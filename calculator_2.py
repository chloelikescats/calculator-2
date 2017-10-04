"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic_2 import *

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")

    num_tokens = map(float, tokens[1:])

    if tokens[0] == "q":
        break

    elif tokens[0] == "+":
        print add(num_tokens)

    elif tokens[0] == "-":
        print subtract(num_tokens)

    elif tokens[0] == "*":
        print multiply(num_tokens)

    elif tokens[0] == "/":
        print divide(num_tokens)

    elif tokens[0] == "square":
        print square(num_tokens)

    elif tokens[0] == "cube":
        print cube(num_tokens)

    elif tokens[0] == "power":
        print power(num_tokens)

    elif tokens[0] == "mod":
        print mod(num_tokens)

    elif tokens[0] == "x+":
        print add_mult(num_tokens)

    elif tokens[0] == "cubes+":
        print add_cubes(num_tokens)

    else:
        print "Please enter valid token or 'q' to quit"    

