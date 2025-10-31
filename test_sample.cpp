#include <iostream>
#include <cmath>
#include <limits>
#include <string>

/**
 * @brief This module provides basic arithmetic operations: addition, subtraction, 
 * multiplication, and division, with a check for division by zero.
 */

/**
 * @brief Adds two numbers.
 * * @param a The first number.
 * @param b The second number.
 * @return The sum of a and b.
 */
double add(double a, double b) {
    return a + b;
}

/**
 * @brief Subtracts the second number from the first.
 * * @param a The number to subtract from (minuend).
 * @param b The number to subtract (subtrahend).
 * @return The difference between a and b.
 */
double subtract(double a, double b) {
    return a - b;
}

/**
 * @brief Multiplies two numbers.
 * * @param a The first number.
 * @param b The second number.
 * @return The product of a and b.
 */
double multiply(double a, double b) {
    return a * b;
}

/**
 * @brief Divides the first number by the second. 
 * Includes a check for division by zero.
 * * @param a The dividend.
 * @param b The divisor.
 * @return The quotient of a and b. Returns NaN (Not a Number) if division by zero occurs.
 */
double divide(double a, double b) {
    if (b == 0.0) {
        // Return Not-a-Number (NaN) to signal an error.
        return std::numeric_limits<double>::quiet_NaN();
    }
    return a / b;
}

/**
 * @brief The main function demonstrates the usage of the arithmetic functions.
 */
int main() {
    std::cout << "--- Basic Arithmetic Demonstrator ---" << std::endl;

    // Example numbers
    double x = 10.0;
    double y = 5.0;
    double z = 0.0;

    // 1. Addition
    double result_add = add(x, y);
    std::cout << "\nAddition: " << x << " + " << y << " = " << result_add << std::endl;

    // 2. Subtraction
    double result_subtract = subtract(x, y);
    std::cout << "Subtraction: " << x << " - " << y << " = " << result_subtract << std::endl;

    // 3. Multiplication
    double result_multiply = multiply(x, y);
    std::cout << "Multiplication: " << x << " * " << y << " = " << result_multiply << std::endl;

    // 4. Division (Normal Case)
    double result_divide_ok = divide(x, y);
    // Check if the result is NaN (error condition)
    if (std::isnan(result_divide_ok)) {
        // This line is technically unreachable for x=10, y=5, but is included for robustness
        std::cout << "Division (OK): " << x << " / " << y << " = " << "Error: Cannot divide by zero." << std::endl;
    } else {
        std::cout << "Division (OK): " << x << " / " << y << " = " << result_divide_ok << std::endl;
    }

    // 5. Division (Division by Zero Check)
    double result_divide_error = divide(x, z);
    // Check if the result is NaN (error condition)
    if (std::isnan(result_divide_error)) {
        // We replicate the Python's explicit error message here
        std::cout << "Division (Error): " << x << " / " << z << " = " << "Error: Cannot divide by zero." << std::endl;
    } else {
        std::cout << "Division (Error): " << x << " / " << z << " = " << result_divide_error << std::endl;
    }

    return 0;
}
