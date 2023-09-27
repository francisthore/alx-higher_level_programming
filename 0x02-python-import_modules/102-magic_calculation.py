#!/user/bin/python3

def magic_calculation(a, b):
    if a < b:
        add = __import__('102-magic_calculation').add
        return add(a, b)
    return a - b
