# As Fast as Possible" (Default Environment):

# Environment: simpy.Environment()
# Behavior: In the default environment, the simulation progresses as quickly as the computer can execute the simulation steps. Time in the simulation does not correspond to real-world time; rather, it advances based on the events and processes in the simulation.
# Use Case: This approach is often used when you are interested in the relative timing of events within the simulation, and the goal is to observe the system's behavior without regard to real-world time.

import simpy

env = simpy.Environment()

def process(env):
    yield env.timeout(1)
    print(f"Simulation time: {env.now}")

env.process(process(env))
env.run(until=10)

# In this example, the simulation time advances rapidly based on the events in the simulation, and the output will show the simulation time, not real-world time.
