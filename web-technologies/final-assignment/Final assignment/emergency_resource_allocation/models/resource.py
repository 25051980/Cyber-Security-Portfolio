# === models/resource.py ===
class Resource:
    def __init__(self, id, resource_type, location):
        self.id = id
        self.resource_type = resource_type
        self.location = location
        self.available = True