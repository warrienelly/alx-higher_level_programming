#!/usr/bin/python3
from add_0 import add

def main():
    a = 1
    b = 2

    output = add(a, b)
    print('{:d} + {:d} = {:d}'.format(a, b, output))

if __name__ == "__main__":
    main()
