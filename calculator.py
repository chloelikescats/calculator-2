"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")

    if tokens[0] == "q":
        break

    elif tokens[0] == "+":
        print add(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "-":
        print subtract(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "*":
        print multiply(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "/":
        print divide(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "square":
        print square(float(tokens[1]))

    elif tokens[0] == "cube":
        print cube(float(tokens[1]))

    elif tokens[0] == "power":
        print power(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "mod":
        print mod(float(tokens[1]), float(tokens[2]))

    elif tokens[0] == "x+":
        print add_mult(float(tokens[1]), float(tokens[2]), float(tokens[3]))

    elif tokens[0] == "cubes+":
        print add_cubes(float(tokens[1]), float(tokens[2]))

    else:
        print "Please enter valid token or 'q' to quit"    



