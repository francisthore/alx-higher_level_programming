#!/user/bin/python3

def magic_calculation(a, b):
    add, sub = None, None

    if a < b:
        add = __import__('magic_calculation_102').add
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    return __import__('magic_calculation_102').sub(a, b)
