class ConsoleView:
    def display_menu(self):
        print("\n--- Emergency Response System ---")
        print("1. Add Incident")
        print("2. Add Resource")
        print("3. View Status")
        print("4. Allocate Resources")
        print("5. Reallocate Resources")
        print("6. Update Incident Priority")
        print("7. Close Incident")
        print("8. Exit")
        return input("Choose an option: ")

    def get_incident_input(self):
        id = input("Incident ID: ")
        location = input("Location (as a number): ")
        emergency_type = input("Type of emergency: ")
        priority = input("Priority (high, medium, low): ").lower()
        while priority not in ["high", "medium", "low"]:
            priority = input("Invalid priority. Enter high, medium, or low: ").lower()
        resources = input("Required resources (comma-separated): ").split(",")
        resources = [r.strip() for r in resources]
        return id, location, emergency_type, priority, resources

    
    def display_status(self, incident_manager, resource_manager):
        print("\n--- Current Incidents ---")
        if not incident_manager.incidents:
            print("No incidents.")
        for inc in incident_manager.incidents:
            allocated_ids = [res.id for res in inc.allocated_resources]
            print(f"ID: {inc.id}, Location: {inc.location}, Type: {inc.emergency_type}, "
                  f"Priority: {inc.priority}, Required: {inc.required_resources}, "
                  f"Allocated: {allocated_ids}")

        print("\n--- Available Resources ---")
        if not resource_manager.resources:
            print("No resources.")
        for res in resource_manager.resources:
            status = "Available" if res.available else "Busy"
            print(f"ID: {res.id}, Type: {res.resource_type}, Location: {res.location}, Status: {status}")

    def get_resource_input(self):
        id = input("Enter Resource ID: ")
        resource_type = input("Enter Resource Type (e.g., ambulance, fire truck): ")

        location = input("Enter Location (zone number): ")
        while not location.isdigit():
            location = input("Invalid input. Location must be a number: ")
        location = int(location)

        return id, resource_type, location
