"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    return num1 + num2


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2


def multiply(num1, num2):
    """Multiply the two inputs together."""
    return num1 * num2

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    return float(num1) / num2

def square(num1):
    """Return the square of the input."""
    return num1 * num1

def cube(num1):
    """Return the cube of the input."""
    return num1 ** 3

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return num1 ** num2

def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2

def add_mult(num1, num2, num3):
    """Takes three numbers, adds the first two,
    then multiplies the sum with the third."""
    return (num1 + num2) * num3


def add_cubes(num1, num2):
    """takes two numbers and returns the sum of their cubes."""

    return cube(num1) + cube(num2)

