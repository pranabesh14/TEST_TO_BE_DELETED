"""
This module provides basic arithmetic operations: addition, subtraction, 
multiplication, and division, with a check for division by zero.
"""

def add(a: float, b: float) -> float:
    """
    Adds two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtracts the second number from the first.

    Args:
        a: The number to subtract from (minuend).
        b: The number to subtract (subtrahend).

    Returns:
        The difference between a and b.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b

def divide(a: float, b: float) -> float or str:
    """
    Divides the first number by the second. Includes a check for division by zero.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The quotient of a and b, or a string error message if division by zero occurs.
    """
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def main():
    """
    The main function demonstrates the usage of the arithmetic functions.
    """
    print("--- Basic Arithmetic Demonstrator ---")

    # Example numbers
    x = 10
    y = 5
    z = 0

    # 1. Addition
    result_add = add(x, y)
    print(f"\nAddition: {x} + {y} = {result_add}")

    # 2. Subtraction
    result_subtract = subtract(x, y)
    print(f"Subtraction: {x} - {y} = {result_subtract}")

    # 3. Multiplication
    result_multiply = multiply(x, y)
    print(f"Multiplication: {x} * {y} = {result_multiply}")

    # 4. Division (Normal Case)
    result_divide_ok = divide(x, y)
    print(f"Division (OK): {x} / {y} = {result_divide_ok}")

    # 5. Division (Division by Zero Check)
    result_divide_error = divide(x, z)
    print(f"Division (Error): {x} / {z} = {result_divide_error}")

# Standard Python idiom to call the main function when the script is executed
if __name__ == "__main__":
    main()
