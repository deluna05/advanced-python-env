a = input().strip()
b = input().strip()

m = len(b)
bb = b + b

shifts = set()
for i in range(len(b)):
    shifts.add(bb[i:i+m])

ans = 0
for i in range(len(a) - m + 1):
    if a[i:i+m] in shifts:
        ans += 1

print(ans)
