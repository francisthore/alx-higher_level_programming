#!/usr/bin/python3

def main():
    import hidden_4
    from builtins import dir

    mods = dir(hidden_4)

    for i in range(0, len(mods)):
        if '__' in mods[i]:
            continue
        else:
            print(mods[i])


if __name__ == '__main__':
    main()
