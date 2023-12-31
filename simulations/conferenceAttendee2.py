from random import randint
import simpy

# Global variables
SIM_TIME = 220
TALK_LENGTH = 30
BREAK_LENGTH = 15
TALKS_PER_SESSION = 3
DURATION_EAT = 3
BUFFET_SLOTS = 1

def attendee(env, name, buffet, knowledge=0, hunger=0):
    while True:
        # Attend talks
        for i in range(TALKS_PER_SESSION):
            # Increment knowledge and hunger based on random values
            knowledge += randint(1, 3) / (1 + hunger)
            hunger += randint(1, 4)
            # Attend a talk for TALK_LENGTH time units
            yield env.timeout(TALK_LENGTH)

        # Display attendee's information after the session of talks
        print("Attendee %s finished session with knowledge %.2f and hunger %.2f" % (name, knowledge, hunger))

        # Go to buffet
        start = env.now
        with buffet.request() as req:
            # Wait for either the buffet request or a timeout (break length minus eating duration)
            yield req | env.timeout(BREAK_LENGTH - DURATION_EAT)
            time_left = BREAK_LENGTH - (env.now - start)

            if req.triggered:
                # If the buffet request was triggered, attendee gets food
                food = min(randint(3, 12), time_left)
                # Less time -> less food
                yield env.timeout(DURATION_EAT)
                hunger -= min(food, hunger)
                time_left -= DURATION_EAT
                print('Attendee %s finished eating with hunger %.2f' % (name, hunger))
            else:
                # If the timeout occurred, attendee didn't make it to the buffet (penalty)
                hunger += 1
                print('Attendee %s didn’t make it to the buffet, hunger is now at %.2f.' % (name, hunger))

        # Take the remaining break time after buffet
        yield env.timeout(time_left)

# Create a SimPy environment
env = simpy.Environment()

# Create a buffet resource with specified capacity
buffet = simpy.Resource(env, capacity=BUFFET_SLOTS)

# Create and run processes for 5 attendees
for i in range(5):
    env.process(attendee(env, i, buffet))

# Run the simulation until SIM_TIME
env.run(until=SIM_TIME)
