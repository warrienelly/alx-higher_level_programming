#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
from sys import argv


def main():
    args = argv[1:]
    if len(args) != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    if args[1] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(args[0])
    b = int(args[2])

    if args[1] == "+":
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))

    if args[1] == "-":
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))

    if args[1] == "*":
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))

    if args[1] == "/":
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))


if __name__ == '__main__':
    main()
