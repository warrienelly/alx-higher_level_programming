#!/usr/bin/python3
def main():
    import sys
    args = sys.argv
    if len(args) != 1:
        if len(args) == 2:
            print('{} argument:'.format(len(args) - 1))
        else:
            print('{} arguments:'.format(len(args) - 1))
        for index in range(len(args[1:])):
            print('{}: {}'.format(index + 1, args[index + 1]))
    else:
        print('{} arguments.'.format(len(args) - 1))


if __name__ == "__main__":
    main()
