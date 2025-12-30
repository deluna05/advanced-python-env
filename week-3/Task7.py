def tr(x, y):
    return x * y / 2

def rec(x, y):
    return x * y

X = float(input())
Y = float(input())
Z = float(input())
T = float(input())

print(tr(X, Y) + rec(Z, T))

n = int(input())
s = oct(n)[2:]
print(s.zfill(10))
