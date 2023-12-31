import simpy
from random import randint

def speaker(env):
    try:
        # Simulate the speaker talking for a random duration between 25 and 35 time units
        yield env.timeout(randint(25, 35))
    except simpy.Interrupt as interrupt:
        # Handle the interrupt and print the cause
        print(interrupt.cause)

def moderator(env):
    for i in range(3):
        # Start the speaker process
        speaker_proc = env.process(speaker(env))
        
        # Use a condition event to either wait for the speaker or a timeout of 30 time units
        results = yield speaker_proc | env.timeout(30)
        # The line results = yield speaker_proc | env.timeout(30) effectively says "wait until either the speaker_proc process completes or 30 time units pass."
        
        # Check if the speaker process is not in the results, then interrupt with a custom cause
        if speaker_proc not in results:
            speaker_proc.interrupt('No time left')
        # his part of the code checks whether the speaker_proc process is not in the results of the condition event. If speaker_proc is not in the results, it means that the condition event was triggered by the timeout (env.timeout(30)) rather than the completion of the speaker_proc process. In this case, the speaker_proc process is interrupted with a custom cause.    

# Create a SimPy environment
env = simpy.Environment()

# Run the moderator process in the environment
env.process(moderator(env))

# Run the simulation until there are no more events
env.run()
