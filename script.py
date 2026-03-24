def sum(a, b):
    return a + b

def devide(a, b):
    if b == 0:
        raise ValueError("Denominator could not be zero!!!")
    if isinstance(a, str) or isinstance(b, str):
        raise ValueError("Error!")
    if isinstance(a, list) or isinstance(b, list):
        raise ValueError("Error_number_2")
    return a / b

def mul(a, b):
    return a * b
