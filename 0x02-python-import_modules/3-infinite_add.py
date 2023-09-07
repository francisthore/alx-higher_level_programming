#!/usr/bin/python3

def main():
    import sys

    argv = sys.argv
    result = 0

    for i in range(1, len(argv)):
        result += int(argv[i])
    print(result)


if __name__ == '__main__':
    main()
