import math

def h(a, b):
    return math.sqrt(a*a + b*b)

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

h1 = h(a1, b1)
h2 = h(a2, b2)

if h1 > h2:
    print(h1, h2)
elif h2 > h1:
    print(h2, h1)
else:
    print("equal")

s = input().split()
r = []
for w in s:
    r.append("".join(sorted(w)))
print(" ".join(r))
