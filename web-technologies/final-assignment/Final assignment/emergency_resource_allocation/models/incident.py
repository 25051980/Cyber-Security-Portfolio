# === models/incident.py ===
class Incident:
    def __init__(self, id, location, emergency_type, priority, required_resources):
        self.id = id
        self.location = location
        self.emergency_type = emergency_type
        self.priority = priority
        self.required_resources = required_resources
        self.allocated_resources = []
        self.status = "open"