# fibonacci

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

# Specify the number of terms you want in the Fibonacci series
num_terms = 10
fib_series = fibonacci(num_terms)

print(f"Fibonacci series with {num_terms} terms: {fib_series}")