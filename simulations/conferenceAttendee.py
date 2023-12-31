from random import randint
import simpy

# global variables
SIM_TIME = 220
TALK_LENGHT = 30
BREAK_LENGTH = 15
TALKS_PER_SESSION = 3

def attendee(env, name, knowledge=0, hunger=0):
    while True:
        # visit talks
        for i in range(TALKS_PER_SESSION):
            knowledge += randint(0.0001, 3) / (1 + hunger)
            hunger += randint(1, 4)
            yield env.timeout(TALK_LENGHT)
        
        print("Attendee %s finished session with knowledge %.2f and hunger %.2f" % (name, knowledge, hunger))
        
        # go for a break
        food = randint(3,12)
        hunger -= min(food, hunger)
        yield env.timeout(BREAK_LENGTH)
        print("Attendee %s finished break with hunger %.2f" % (name, hunger)) 
        
        
env = simpy.Environment()
for i in range(5):
    env.process(attendee(env, i))
env.run(until=SIM_TIME)             