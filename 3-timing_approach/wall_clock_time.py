# "Synchronized with Wall-Clock Time" (RealtimeEnvironment):

# Environment: simpy.RealtimeEnvironment()
# Behavior: In a RealtimeEnvironment, the simulation is synchronized with the wall-clock time. The simulation progresses in real-world time, and the timing of events in the simulation corresponds to actual time.
# Use Case: This approach is useful when you want to simulate a system in real-time, and you want the simulation to reflect the passage of time similar to a clock on the wall.

import simpy

env = simpy.RealtimeEnvironment()

def process(env):
    yield env.timeout(1)
    print(f"Real-world time: {env.now}")

env.process(process(env))
env.run(until=10)

# In this example, even though the simulation time advances based on the events, the output will show real-world time, making it suitable for simulations where timing is critical and should correspond to the actual passage of time.
