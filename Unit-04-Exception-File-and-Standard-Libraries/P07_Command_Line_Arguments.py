# Unit 4 - P07
# Program to perform arithmetic operation using command line arguments
# How to run:  python P07_Command_Line_Arguments.py 10 5 +
# For multiplication use quotes:  python P07_Command_Line_Arguments.py 10 5 "*"

import sys

if len(sys.argv) != 4:
    print("Usage: python P07_Command_Line_Arguments.py <number1> <number2> <operator>")
else:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    op = sys.argv[3]

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b == 0:
            print("Error: division by zero is not possible")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operator! Use +, -, * or /")
