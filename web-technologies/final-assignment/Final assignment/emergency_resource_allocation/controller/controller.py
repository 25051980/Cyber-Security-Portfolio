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
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please try again.")
