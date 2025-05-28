def factorial(n):
    """Calculate the factorial of a given number using iteration"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Calculate factorial of 5
print(f"The factorial of 5 is {factorial(5)}")