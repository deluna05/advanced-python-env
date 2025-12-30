def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A = int(input())
B = int(input())
C = int(input())
D = int(input())

n = A * D - C * B
d = B * D
g = gcd(abs(n), d)
print(n // g, d // g)

x = int(input())
for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=" ")
