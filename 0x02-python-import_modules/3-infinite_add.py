#!/usr/bin/python3
import sys


def main():
    args = sys.argv
    sum_value = 0

    if len(args) != 1:
        for arg in args[1:]:
            sum_value = sum_value + int(arg)

        print(sum_value)


if __name__ == "__main__":
    main()
