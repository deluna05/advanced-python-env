import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A = int(input())
B = int(input())

g = gcd(A, B)
print(g, A * B // g)

a = float(input())
b = float(input())
c = float(input())
d = float(input())
di = float(input())

p1 = (a + b + di) / 2
s1 = math.sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - di))

p2 = (c + d + di) / 2
s2 = math.sqrt(p2 * (p2 - c) * (p2 - d) * (p2 - di))

print(s1 + s2)
