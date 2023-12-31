import random
import simpy
import numpy as np

# Global variables
NUM_EMPLOYEES = 2
AVG_SERVICE_TIME = 5
CUSTOMER_INTERVAL_TIME = 2
SIM_TIME = 120

customer_handled = 0

class CallCenter:
    
    def __init__(self, env, num_employees, avg_service_time):
        # Constructor for the CallCenter class
        self.env = env
        # Create a Resource named staff with the given number of employees
        self.staff = simpy.Resource(env, num_employees)
        # Average service time for customer support
        self.avg_service_time = avg_service_time
        
    def support(self, customer):
        # Function representing the customer support process
        # Generate a random service time based on a normal distribution
        random_time = max(1, np.random.normal(self.avg_service_time, 4))
        # Simulate the support process by waiting for the generated time
        yield self.env.timeout(random_time)
        print(f"Support finished for {customer} at {self.env.now:.2f}")
        
        
def customer(env, name, call_center):
    # Function representing a customer arriving at the call center
    global customer_handled
    print(f"Customer {name} arrives at the call center at {env.now:.2f}")
    # Request the staff resource to start the support process
    with call_center.staff.request() as request:
        yield request
        print(f"{name} enters the call at {env.now:.2f}")
        # Start the support process using the CallCenter's support function
        yield env.process(call_center.support(name))
        print(f"{name} leaves the call center at {env.now:.2f}")
        customer_handled += 1
        
def setup(env, num_employees, avg_service_time, customer_interval_time):
    # Function to set up the simulation environment
    call_center = CallCenter(env, num_employees, avg_service_time)
    
    # Create initial customers and start their processes
    for i in range(1, 6):
        env.process(customer(env, i, call_center))
        
    # Continuously generate new customers at random intervals
    while True:
        yield env.timeout(random.randint(customer_interval_time - 1, customer_interval_time + 1))
        i += 1
        env.process(customer(env, i, call_center))
        
# Main simulation code
print("Starting the call center simulation...")

# Create a SimPy environment
env = simpy.Environment()

# Start the setup process to initialize the simulation
env.process(setup(env, NUM_EMPLOYEES, AVG_SERVICE_TIME, CUSTOMER_INTERVAL_TIME))

# Run the simulation until SIM_TIME
env.run(until=SIM_TIME)

# Display the total number of customers handled during the simulation
print(f"Total customers handled: {customer_handled}")
