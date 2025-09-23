# 代码生成时间: 2025-09-24 00:03:27
import scrapy
def add(a, b):
    """Add two numbers.

    Args:
        a (float): First operand.
        b (float): Second operand.

    Returns:
        float: Sum of a and b.
    """
    return a + b
def subtract(a, b):
    """Subtract two numbers.

    Args:
        a (float): Minuend.
        b (float): Subtrahend.

    Returns:
        float: Difference of a and b.
    """
    return a - b
def multiply(a, b):
    """Multiply two numbers.

    Args:
        a (float): First multiplicand.
        b (float): Second multiplicand.

    Returns:
        float: Product of a and b.
    """
    return a * b
def divide(a, b):
    """Divide two numbers.

    Args:
        a (float): Dividend.
        b (float): Divisor.

    Returns:
        float: Quotient of a and b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
def power(a, b):
    """Raise a to the power of b.

    Args:
        a (float): Base.
        b (float): Exponent.

    Returns:
        float: a raised to the power of b.
    """
    return a ** b
def main():
    # Test the math functions
    print("Addition: 3 + 2 =", add(3, 2))
    print("Subtraction: 5 - 2 =", subtract(5, 2))
    print("Multiplication: 4 * 3 =", multiply(4, 3))
    try:
        print("Division: 10 / 2 =", divide(10, 2))
    except ZeroDivisionError as e:
        print(e)
    print("Power: 2 ** 3 =", power(2, 3))
if __name__ == "__main__":
    main()