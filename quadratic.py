import math

def roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "( )"
    r1 = (-b + math.sqrt(discriminant)) / (2*a)
    r2 = (-b - math.sqrt(discriminant)) / (2*a)
    if r1 == r2:
        return f"({r1})"
    elif r1 == 0 and r2 == 0:
        return "( )"

    return f"({r1}, {r2})"

def value_y(a, b, c, x):
    return a * x ** 2 + b * x + c

def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    if a==0:
        return f"f(x) = {b}x + {c}"
    if b==0:
        return f"f(x) = {a} * X^2 + {c}"

    return f"f(x) = {a}x**2 + {b}x + {c}"

def derivation(a, b, c):
    if a == 0 and b == 0:
        return f"f'(x) = 0"
    if a==0:
        return f"f'(x) = {b}"
    if b==0:
        return f"f'(x) = {a*2}x"
    return f"f'(x) = {a*2}x + {b}"

