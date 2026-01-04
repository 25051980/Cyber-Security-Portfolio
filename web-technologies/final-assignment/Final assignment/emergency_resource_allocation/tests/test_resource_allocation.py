import unittest
from models.incident import Incident
from models.resource import Resource
from models.incident_manager import IncidentManager
from models.resource_manager import ResourceManager


class TestEmergencySystem(unittest.TestCase):

    def setUp(self):
        # Reset singleton before each test
        ResourceManager._instance = None
        self.resource_manager = ResourceManager.get_instance()
        self.incident_manager = IncidentManager()

    def test_incident_creation(self):
        incident = Incident("I1", 1, "fire", "high", ["ambulance"])
        self.incident_manager.incidents.append(incident)
        self.assertEqual(len(self.incident_manager.incidents), 1)
        self.assertEqual(incident.priority, "high")
        self.assertIn("ambulance", incident.required_resources)

    def test_resource_allocation(self):
        resource = Resource("R1", "ambulance", 1)
        self.resource_manager.resources.append(resource)
        incident = Incident("I2", 1, "crash", "high", ["ambulance"])
        self.incident_manager.incidents.append(incident)

        self.resource_manager.allocate_resources(self.incident_manager)

        self.assertFalse(resource.available)
        self.assertEqual(incident.allocated_resources[0].id, "R1")
       
    def test_resource_reallocation(self):
        # Create a single resource
        resource = Resource("R1", "ambulance", 1)
        self.resource_manager.resources.append(resource)

        # Low-priority incident gets the resource first
        low_incident = Incident("I1", 1, "burn", "low", ["ambulance"])
        self.incident_manager.incidents.append(low_incident)
        self.resource_manager.allocate_resources(self.incident_manager)

        self.assertEqual(low_incident.allocated_resources[0].id, "R1")

        # Now, a high-priority incident comes in
        high_incident = Incident("I2", 2, "heart attack", "high", ["ambulance"])
        self.incident_manager.incidents.append(high_incident)

        # Reallocate resources
        self.resource_manager.reallocate_resources(self.incident_manager)

        # Expect resource to be reallocated to the high-priority incident
        self.assertIn(resource, high_incident.allocated_resources)
        self.assertNotIn(resource, low_incident.allocated_resources)
    
    def test_close_incident_releases_resources(self):
        # Create resource and incident
        resource = Resource("R2", "ambulance", 1)
        self.resource_manager.resources.append(resource)

        incident = Incident("I3", 1, "crash", "medium", ["ambulance"])
        incident.allocated_resources.append(resource)
        self.incident_manager.incidents.append(incident)

        # Mark resource as unavailable (it's in use)
        resource.available = False

        # Close the incident manually (simulate the logic)
        for inc in self.incident_manager.incidents:
            if inc.id == "I3":
                for res in inc.allocated_resources:
                    res.available = True
                self.incident_manager.incidents.remove(inc)
                break

        # Test that the incident was removed and resource is available
        self.assertEqual(len(self.incident_manager.incidents), 0)
        self.assertTrue(resource.available)

    def test_update_incident_priority(self):
        # Create a medium-priority incident
        incident = Incident("I4", 2, "flood", "medium", ["fire truck"])
        self.incident_manager.incidents.append(incident)

        # Simulate priority update logic
        for inc in self.incident_manager.incidents:
            if inc.id == "I4":
                inc.priority = "high"  # Simulating user update

        # Check the priority was updated
        self.assertEqual(incident.priority, "high")
        
if __name__ == '__main__':
    unittest.main()
