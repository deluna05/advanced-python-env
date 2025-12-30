def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A = int(input())
B = int(input())
C = int(input())
D = int(input())

n = A * D
d = B * C
g = gcd(n, d)
print(n // g, d // g)

xa = float(input())
yb = float(input())
R = float(input())

def inside(x, y):
    return (x - xa)**2 + (y - yb)**2 < R**2

cnt = 0
for i in range(3):
    x = float(input())
    y = float(input())
    if inside(x, y):
        cnt += 1

print(cnt)
