# speaker Process:

# The speaker function simulates a speaker who talks for a random duration between 25 and 35 time units.
# If an asynchronous interrupt (simpy.Interrupt) occurs during the talking, the code inside the except block is executed, printing the cause of the interrupt.

# moderator Process:

# The moderator function simulates a moderator interacting with the speaker.
# It runs a loop three times, indicating three interactions with the speaker.
# Inside the loop, it starts the speaker process using env.process(speaker(env)).
# It then yields control for 30 time units before interrupting the speaker process with a custom cause ('No time left').

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
        
        # Yield control for 30 time units
        yield env.timeout(30)
        
        # Interrupt the speaker process with a custom cause
        speaker_proc.interrupt('No time left')

# Create a SimPy environment
env = simpy.Environment()

# Run the moderator process in the environment
env.process(moderator(env))

# Run the simulation until there are no more events
env.run()
