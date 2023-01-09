#!/usr/bin/python3
def main():
    import sys
    args = sys.argv
    if len(args) != 1:
        sum_value = 0
        for arg in args[1:]:
            sum_value = sum_value + int(arg)
        print(sum_value)


if __name__ == "__main__":
    main()
