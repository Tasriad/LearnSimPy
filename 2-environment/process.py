import simpy

def simple_process(env):
    print(f"Process starts at time {env.now}")
    
    # Simulate some activity or computation
    yield env.timeout(3)
    
    print(f"Process resumes at time {env.now}")
    
    # Simulate more activity
    yield env.timeout(2)
    
    print(f"Process completes at time {env.now}")

# Create a SimPy environment
env = simpy.Environment()

# Create and start a process in the environment
env.process(simple_process(env))

# Run the simulation
env.run(until=10)
