# The generator fibonacci_generator produces an infinite sequence of Fibonacci numbers. The use of yield allows you to create a generator that produces values on-the-fly without having to compute the entire sequence in advance.

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create a generator object
fib_gen = fibonacci_generator()

# Print the first 5 Fibonacci numbers
for _ in range(5):
    print(next(fib_gen))
