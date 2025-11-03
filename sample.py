import sys

def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

# ---

def subtract_numbers(a, b):
    """Subtracts the second number from the first and returns the result."""
    return a - b

# ---

def multiply_numbers(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b

# ---

def divide_numbers(a, b):
    """
    Divides the first number by the second.
    Throws a warning and returns None if the divisor is zero.
    """
    if b == 0:
        # Using sys.stderr to print the warning to the standard error stream
        print("⚠️ Warning: Cannot divide by zero!", file=sys.stderr)
        return None
    return a / b

# ---

def main():
    """
    The main function to demonstrate the use of the arithmetic functions.
    """
    # Define some test numbers
    x = 10
    y = 5
    z = 0

    print(f"--- Testing with numbers x={x}, y={y}, z={z} ---")

    ## 1. Addition
    print(f"\n1. Adding {x} and {y}:")
    sum_result = add_numbers(x, y)
    print(f"Result: {sum_result}") # Output: 15

    ## 2. Subtraction
    print(f"\n2. Subtracting {y} from {x}:")
    diff_result = subtract_numbers(x, y)
    print(f"Result: {diff_result}") # Output: 5

    ## 3. Multiplication
    print(f"\n3. Multiplying {x} and {y}:")
    prod_result = multiply_numbers(x, y)
    print(f"Result: {prod_result}") # Output: 50

    ## 4. Division (Successful Case)
    print(f"\n4. Dividing {x} by {y}:")
    div_result_ok = divide_numbers(x, y)
    print(f"Result: {div_result_ok}") # Output: 2.0

    ## 4. Division (Zero-Division Case)
    print(f"\n4. Dividing {x} by {z} (Zero-Division Test):")
    div_result_fail = divide_numbers(x, z)
    # The warning will be printed by the function itself
    print(f"Result: {div_result_fail}") # Output: None

# ---

# Standard Python idiom to call the main function when the script is executed
if __name__ == "__main__":
    main()