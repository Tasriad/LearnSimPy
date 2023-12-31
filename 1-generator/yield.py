# The yield statement in Python is used in the context of defining a generator function. It allows a function to produce a sequence of values over time, rather than computing all of them at once and returning a single result. When a function with yield is called, it returns a generator object, which can be iterated to obtain values one at a time.


def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()

# Iterate over the generator to get values
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
print(next(gen))  # Output: StopIteration exception

# If we try to get the next value, a StopIteration exception will be raised
# because the generator has exhausted its values
# print(next(gen))  # Uncommenting this line would raise StopIteration
