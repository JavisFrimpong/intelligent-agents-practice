import random

class DisasterEnvironment:
    def __init__(self):
        self.severity = 0
        self.disaster_types = ["earthquake", "flood", "fire", "storm", "landslide"]

    def generate_event(self):
        # Randomly choose disaster type
        disaster_type = random.choice(self.disaster_types)
        # Random severity from 1 to 10
        self.severity = random.randint(1, 10)
        # Return both type and severity as a dictionary
        return {"type": disaster_type, "severity": self.severity}
