import math

def tr(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

a = float(input())
print(6 * tr(a, a, a))

for i in range(3):
    x = float(input())
    y = float(input())
    print(x * y)
