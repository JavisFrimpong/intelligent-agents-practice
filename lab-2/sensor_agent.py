from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
import asyncio
from datetime import datetime
from environment import DisasterEnvironment


class SensorBehaviour(CyclicBehaviour):
    async def run(self):
        # Get percept from environment
        percept = self.agent.environment.generate_event()
        disaster_type = percept["type"]
        severity = percept["severity"]

        # Record timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Print percept with timestamp
        print(f"[SensorAgent] [{timestamp}] Detected {disaster_type} with severity: {severity}")

        # Log percept to file
        with open("event_log.txt", "a") as f:
            f.write(f"[{timestamp}] {disaster_type} detected with severity: {severity}\n")

        # Store percept history in agent memory
        if not hasattr(self.agent, "percept_history"):
            self.agent.percept_history = []
        self.agent.percept_history.append((timestamp, disaster_type, severity))

        # Wait before next perception
        await asyncio.sleep(5)


class SensorAgent(Agent):
    async def setup(self):
        print("SensorAgent started")
        self.environment = DisasterEnvironment()
        self.add_behaviour(SensorBehaviour())


async def main():
    # Replace with your XMPP credentials
    agent = SensorAgent("spencer1@xmpp.jp", "Quadjo@23")
    await agent.start(auto_register=True)
    await asyncio.sleep(40)  # Run for 40 seconds
    await agent.stop()


if __name__ == "__main__":
    asyncio.run(main())
