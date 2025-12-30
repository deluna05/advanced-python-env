n = int(input())
for x in range(1, n + 1):
    ok = True
    for d in str(x):
        if d == '0' or x % int(d) != 0:
            ok = False
            break
    if ok:
        print(x, end=" ")
print()

m = int(input())
a = []
for i in range(m):
    a.append(int(input()))

print(a)
a[0], a[-1] = a[-1], a[0]
print(a)
