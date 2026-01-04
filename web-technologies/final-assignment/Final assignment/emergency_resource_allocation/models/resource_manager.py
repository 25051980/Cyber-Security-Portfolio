import os
import pickle
from models.resource import Resource
from patterns.factory import ResourceFactory

class ResourceManager:
    _instance = None

    def __init__(self, filename="resources.pkl"):
        if ResourceManager._instance:
            raise Exception("This class is a singleton!")
        self.filename = filename
        self.resources = self.load_from_file()
        ResourceManager._instance = self

    @staticmethod
    def get_instance():
        if ResourceManager._instance is None:
            ResourceManager()
        return ResourceManager._instance

    def save_to_file(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.resources, f)

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        return []

    def add_resource(self, view):
        id, resource_type, location = view.get_resource_input()

        if any(res.id == id for res in self.resources):
            print(f"A resource with ID '{id}' already exists. Please use a unique ID.")
            return

        resource = Resource(id, resource_type, location)
        self.resources.append(resource)
        self.save_to_file()
        print(f"Resource '{id}' added successfully.")

    def get_nearest_available_resource(self, resource_type, location):
        candidates = [
            r for r in self.resources
            if r.resource_type == resource_type.strip() and r.available
        ]
        candidates.sort(key=lambda r: abs(int(r.location) - int(location)))
        return candidates[0] if candidates else None

    def allocate_resources(self, incident_manager):
        priority_map = {"high": 3, "medium": 2, "low": 1}
        sorted_incidents = sorted(
            incident_manager.incidents,
            key=lambda i: priority_map.get(i.priority.lower(), 0),
            reverse=True
        )
        for incident in sorted_incidents:
            for resource_type in incident.required_resources:
                already_allocated = [
                    r for r in incident.allocated_resources if r.resource_type == resource_type.strip()
                ]
                if already_allocated:
                    continue
                chosen = self.get_nearest_available_resource(resource_type, incident.location)
                if chosen:
                    chosen.available = False
                    incident.allocated_resources.append(chosen)

    def reallocate_resources(self, incident_manager):
        priority_map = {"high": 3, "medium": 2, "low": 1}
        sorted_incidents = sorted(
            incident_manager.incidents,
            key=lambda i: priority_map.get(i.priority.lower(), 0),
            reverse=True
        )
        for incident in sorted_incidents:
            for resource_type in incident.required_resources:
                if any(r.resource_type == resource_type.strip() for r in incident.allocated_resources):
                    continue
                available = [
                    r for r in self.resources
                    if r.resource_type == resource_type.strip() and r.available
                ]
                available.sort(key=lambda r: abs(int(r.location) - int(incident.location)))
                if available:
                    chosen = available[0]
                    chosen.available = False
                    incident.allocated_resources.append(chosen)
                    print(f"Allocated available resource {chosen.id} to Incident {incident.id}")
                    continue
                for other_incident in reversed(sorted_incidents):
                    if priority_map[other_incident.priority.lower()] < priority_map[incident.priority.lower()]:
                        for r in other_incident.allocated_resources:
                            if r.resource_type == resource_type.strip():
                                other_incident.allocated_resources.remove(r)
                                incident.allocated_resources.append(r)
                                print(f"Reallocated resource {r.id} from Incident {other_incident.id} to Incident {incident.id}")
                                return
