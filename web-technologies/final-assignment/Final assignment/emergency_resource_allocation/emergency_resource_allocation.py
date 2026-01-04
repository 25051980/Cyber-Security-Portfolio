# === emergency_resource_allocation/main.py ===
from controller.controller import Controller

def main():
    controller = Controller()
    controller.run()

if __name__ == "__main__":
    main()

# === emergency_resource_allocation/controllers/controller.py ===
from models.incident_manager import IncidentManager
from models.resource_manager import ResourceManager
from views.console_view import ConsoleView

class Controller:
    def __init__(self):
        self.view = ConsoleView()
        self.incident_manager = IncidentManager()
        self.resource_manager = ResourceManager.get_instance()

    def run(self):
        while True:
            choice = self.view.display_menu()
            if choice == "1":
                self.incident_manager.add_incident(self.view)
            elif choice == "2":
                self.resource_manager.add_resource(self.view)
            elif choice == "3":
                self.view.display_status(self.incident_manager, self.resource_manager)
            elif choice == "4":
                self.resource_manager.allocate_resources(self.incident_manager)
            elif choice == "5":
                self.resource_manager.reallocate_resources(self.incident_manager)
            elif choice == "6":
                self.incident_manager.update_incident_priority(self.view)
            elif choice == "7":
                self.incident_manager.close_incident()
            elif choice == "8":
                break

# === emergency_resource_allocation/models/incident.py ===
class Incident:
    def __init__(self, id, location, emergency_type, priority, required_resources):
        self.id = id
        self.location = location
        self.emergency_type = emergency_type
        self.priority = priority
        self.required_resources = required_resources
        self.allocated_resources = []

# === emergency_resource_allocation/models/resource.py ===
class Resource:
    def __init__(self, id, resource_type, location):
        self.id = id
        self.resource_type = resource_type
        self.location = location
        self.available = True

# === emergency_resource_allocation/models/incident_manager.py ===
from models.incident import Incident
from patterns.factory import IncidentFactory

class IncidentManager:
    def __init__(self):
        self.incidents = []

    def add_incident(self, view):
        id = input("Incident ID: ")

    # Check for duplicate ID
        if any(inc.id == id for inc in self.incidents):
            print(f"An incident with ID '{id}' already exists. Please use a unique ID.")
            return

        incident = IncidentFactory.create_from_input(view)
        self.incidents.append(incident)

    def close_incident(self):
        incident_id = input("Enter the ID of the incident to close: ")
        for inc in self.incidents:
            if inc.id == incident_id:
                # Release the allocated resources
                for res in inc.allocated_resources:
                    res.available = True
                self.incidents.remove(inc)
                print(f"Incident {incident_id} closed and resources released.")
                return
        print("Incident not found.")

# === emergency_resource_allocation/models/resource_manager.py ===
from models.resource import Resource
from patterns.factory import ResourceFactory

class ResourceManager:
    _instance = None

    def __init__(self):
        if ResourceManager._instance:
            raise Exception("This class is a singleton!")
        self.resources = []
        ResourceManager._instance = self

    @staticmethod
    def get_instance():
        if not ResourceManager._instance:
            ResourceManager()
        return ResourceManager._instance

    def add_resource(self, view):
        id = input("Resource ID: ")

        if any(res.id == id for res in self.resources):
            print(f"A resource with ID '{id}' already exists. Please use a unique ID.")
            return

        resource = ResourceFactory.create_from_input(view)
        self.resources.append(resource)

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
    
        # Sort incidents from high to low priority
        sorted_incidents = sorted(
            incident_manager.incidents,
            key=lambda i: priority_map.get(i.priority.lower(), 0),
            reverse=True
        )

        for incident in sorted_incidents:
            for resource_type in incident.required_resources:
                # Skip if already allocated
                if any(r.resource_type == resource_type.strip() for r in incident.allocated_resources):
                    continue

                # Step 1: Try to allocate from available resources
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

                # Step 2: Reallocate from lower-priority incidents
                for other_incident in reversed(sorted_incidents):  # Start from lowest priority
                    if priority_map[other_incident.priority.lower()] < priority_map[incident.priority.lower()]:
                        for r in other_incident.allocated_resources:
                            if r.resource_type == resource_type.strip():
                                # Reallocate
                                other_incident.allocated_resources.remove(r)
                                incident.allocated_resources.append(r)
                                print(f"Reallocated resource {r.id} from Incident {other_incident.id} to Incident {incident.id}")
                                return  # stop after one successful reallocation

    def update_incident_priority(self, view):
        incident_id = input("Enter the Incident ID to update: ")
        for inc in self.incidents:
            if inc.id == incident_id:
                print(f"Current Priority: {inc.priority}")
                new_priority = input("Enter new priority (high, medium, low): ").lower()
                while new_priority not in ["high", "medium", "low"]:
                    new_priority = input("Invalid input. Enter new priority (high, medium, low): ").lower()
                inc.priority = new_priority
                print(f"Incident {incident_id} priority updated to {new_priority}.")
                return
        print(f"Incident with ID {incident_id} not found.")


# === emergency_resource_allocation/views/console_view.py ===
class ConsoleView:
    def display_menu(self):
        print("""
        === Emergency Resource Allocation ===
        1. Add Incident
        2. Add Resource
        3. View Status
        4. Allocate Resources
        5. Reallocate Resources
        6. Update Incident Priority
        7. Close Incident
        8. Exit
        """)
        return input("Select an option: ")

    def display_status(self, incident_manager, resource_manager):
        print("\n=== INCIDENTS STATUS ===")
        print(f"{'ID':<10} {'Location':<10} {'Priority':<10} {'Required':<25} {'Allocated':<25}")
        print("-" * 80)
        for inc in incident_manager.incidents:
            required = ', '.join(inc.required_resources)
            allocated = ', '.join([r.id for r in inc.allocated_resources])
            print(f"{inc.id:<10} {str(inc.location):<10} {inc.priority:<10} {required:<25} {allocated:<25}")

        print("\n=== RESOURCES STATUS ===")
        print(f"{'ID':<10} {'Type':<15} {'Location':<10} {'Status':<10}")
        print("-" * 50)
        for res in resource_manager.resources:
            status = "Available" if res.available else "Busy"
            print(f"{res.id:<10} {res.resource_type:<15} {str(res.location):<10} {status:<10}")

# === emergency_resource_allocation/patterns/factory.py ===
from models.incident import Incident
from models.resource import Resource

class IncidentFactory:
    @staticmethod
    def create_from_input(view):
        id = input("Incident ID: ")

        location = input("Location (zone number): ")
        while not location.isdigit():
            location = input("Invalid. Location must be a number: ")
        location = int(location)

        emergency_type = input("Emergency Type: ")

        priority = input("Priority (high, medium, low): ").lower()
        while priority not in ["high", "medium", "low"]:
            priority = input("Invalid. Enter priority (high, medium, low): ").lower()

        required_resources = input("Required Resources (comma separated): ").split(",")
        required_resources = [res.strip() for res in required_resources if res.strip()]

        while not required_resources:
            print("You must specify at least one required resource.")
            required_resources = input("Required Resources (comma separated): ").split(",")
            required_resources = [res.strip() for res in required_resources if res.strip()]
            return Incident(id, location, emergency_type, priority, required_resources)

class ResourceFactory:
    @staticmethod
    def create_from_input(view):
        id = input("Resource ID: ")
        resource_type = input("Resource Type (ambulance, fire truck, etc): ")

        location = input("Location (zone number): ")
        while not location.isdigit():
            location = input("Invalid. Location must be a number: ")
        location = int(location)

        return Resource(id, resource_type, location)

# === emergency_resource_allocation/patterns/observer.py ===
# Placeholder for Observer pattern if you wish to expand it later (e.g., notify views or logs on state change)
class Observer:
    def update(self):
        pass

