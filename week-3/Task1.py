import math

c = int(input())
if c == 1:
    r = float(input())
    print(math.pi * r * r)
elif c == 2:
    a = float(input())
    b = float(input())
    print(a * b)
elif c == 3:
    a = float(input())
    h = float(input())
    print(a * h / 2)

for i in range(3):
    n = int(input())
    s = 0
    for j in range(n):
        s += int(input())
    print(s, s / n)
