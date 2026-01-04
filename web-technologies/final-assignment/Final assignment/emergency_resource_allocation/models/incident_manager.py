# === models/incident_manager.py ===

from models.incident import Incident
from patterns.factory import IncidentFactory
import os
import pickle

class IncidentManager:
    def __init__(self, filename="incidents.txt"):
        self.filename = filename
        self.incidents = self.load_from_file()

    def add_incident(self, view):
        id = input("Incident ID: ")
        if any(inc.id == id for inc in self.incidents):
            print(f"An incident with ID '{id}' already exists. Please use a unique ID.")
            return

        # ✅ Create incident and check if it was successful
        incident = IncidentFactory.create_from_input(view, id)
        if incident is None:
            print("Incident creation was cancelled or failed.")
            return  # Don't continue if something went wrong

        self.incidents.append(incident)
        self.save_to_file()
        print(f"Incident '{incident.id}' added successfully.")

    def close_incident(self):
        incident_id = input("Enter the ID of the incident to close: ")
        self.incidents = self.load_from_file()  # Reload from file to get latest data
        found = False
        for inc in self.incidents:
            if inc.id == incident_id:
                inc.status = "closed"
                found = True
                print(f"Incident {incident_id} marked as closed.")
                break
        if found:
            self.save_to_file()
        else:
            print(f"No incident with ID '{incident_id}' was found.")

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
    
    def save_to_file(self, filename=None):
        filename = filename or self.filename
        with open(filename, "w") as f:
            for incident in self.incidents:
                allocated_ids = [res.id for res in incident.allocated_resources]
                line = (
                    f"ID: {incident.id}, "
                    f"Location: {incident.location}, "
                    f"Type: {incident.emergency_type}, "
                    f"Priority: {incident.priority}, "
                    f"Required: {incident.required_resources}, "
                    f"Allocated: {allocated_ids}, "
                    f"Status: {getattr(incident, 'status', 'open')}"
                )
                f.write(line + "\n")

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return []

        incidents = []
        with open(self.filename, "r") as f:
            lines = f.readlines()

        for line in lines:
            if not line.strip():
                continue
            parts = line.strip().split(", ")
            data = {}
            for part in parts:
                key, value = part.split(": ", 1)
                data[key.lower()] = value

            required = eval(data["required"])
            allocated = eval(data["allocated"])

            incident = Incident(
                id=data["id"],
                location=data["location"],
                emergency_type=data["type"],
                priority=data["priority"],
                required_resources=required,
            )
            incident.allocated_resources = []  # Optionally rebuild from allocated
            incident.status = data.get("status", "open")
            incidents.append(incident)

        return incidents
