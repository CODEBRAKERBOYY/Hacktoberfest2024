def fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence up to n terms.
    
    :param n: Number of terms in the sequence
    :return: A list containing the Fibonacci sequence
    """
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
        
    return sequence

# Get number of terms from the user
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Generate the Fibonacci sequence
fib_sequence = fibonacci_sequence(num_terms)

# Print the sequence
print(f"Fibonacci sequence with {num_terms} terms: {fib_sequence}")
