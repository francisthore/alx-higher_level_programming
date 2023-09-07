#!/usr/bin/python3

def print_args(argv):
    """My function to print args

    Args:
        argv: a list of cmd args
    """
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))


def main():
    import sys

    argv = sys.argv
    num_args = len(argv)

    if num_args == 1:
        print("0 arguments.")
    elif num_args == 2:
        print("1 argument:")
        print_args(argv)
    else:
        print("{} arguments:".format(num_args - 1))
        print_args(argv)


if __name__ == '__main__':
    main()
