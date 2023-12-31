# The Environment class in SimPy represents the simulation environment. It is the container for all simulation processes and provides the framework for managing the simulation timeline and events.

# The Environment class is where you create and run simulation processes. It manages the simulation time, allows you to schedule events, and provides facilities for processes to interact with the environment.

# env.timeout(t) is a convenience method provided by SimPy for creating a timeout event. It represents a delay or time interval after which a process will resume execution.

# yield env.timeout(3)  # Pause the process for 3 simulation time units

# The timeout method is used in a process to introduce a delay. When a process encounters yield env.timeout(t), it temporarily yields control to the simulation environment for t time units. After the specified time has passed, the process resumes execution.

# Processes are the building blocks of SimPy simulations. They are created using Python generator functions. When you start a process using env.process(my_process(env)), it becomes part of the simulation and can interact with the environment, yield for timeouts, and perform various actions.

import simpy

def clock(env, name, tick):
    while True:
        # Print the name of the clock and the current simulation time
        print(name, env.now)
        
        # Yield an event representing the passage of time (timeout) with the specified tick
        yield env.timeout(tick)

# Create a SimPy environment
env = simpy.Environment()

# Start two clock processes with different tick rates
env.process(clock(env, 'fast', 0.5))
env.process(clock(env, 'slow', 1))

# Run the simulation until the specified time (2 in this case)
env.run(until=2)
