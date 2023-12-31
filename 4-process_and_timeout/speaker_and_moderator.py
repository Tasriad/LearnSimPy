import simpy

def speaker(env):
    # The speaker process yields a timeout event representing 30 time units of talking
    yield env.timeout(30)
    # After talking, the speaker returns a 'handout'
    return 'handout'

def moderator(env):
    for i in range(3):
        # Start the speaker process and yield control until it completes
        val = yield env.process(speaker(env))
        # Print the result returned by the speaker process
        print(f"Moderator received: {val}")

# Create a SimPy environment
env = simpy.Environment()

# Run the moderator process in the environment
env.process(moderator(env))

# Run the simulation until there are no more events
env.run()
