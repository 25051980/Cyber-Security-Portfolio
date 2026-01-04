from models.incident import Incident
from models.resource import Resource

from models.incident import Incident
from models.resource import Resource

class IncidentFactory:
    @staticmethod
    def create_from_input(view, id):  # ID is passed from IncidentManager
        location = input("Location (zone number): ")
        while not location.isdigit():
            location = input("Invalid. Location must be a number: ")
        location = int(location)

        emergency_type = input("Emergency Type: ")

        # ✅ Priority input fixed with strip().lower()
        priority = input("Priority (high, medium, low): ").strip().lower()
        while priority not in ["high", "medium", "low"]:
            priority = input("Invalid. Enter priority (high, medium, low): ").strip().lower()

        # ✅ Required resources input with error handling
        while True:
            try:
                raw_input_resources = input("Required Resources (comma separated): ").strip()
                if not raw_input_resources:
                    print("You must specify at least one required resource.")
                    continue

                required_resources = [res.strip() for res in raw_input_resources.split(",") if res.strip()]
                if required_resources:
                    break
                else:
                    print("You must specify at least one valid resource.")
            except EOFError:
                print("\nInput cancelled. Exiting resource entry.")
                return None

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

def add_resource(self, view):
    id, _, _ = view.get_resource_input()
    if any(res.id == id for res in self.resources):
        print(f"A resource with ID '{id}' already exists. Please use a unique ID.")
        return

    resource = ResourceFactory.create_from_input(view)
    self.resources.append(resource)
    print(f"Resource '{resource.id}' added successfully.")
