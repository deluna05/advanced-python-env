N = int(input())

total = 0

if N >= 1:
    i = 1
    while i <= N:
        total = total + i
        i = i + 1
else:
    i = N
    while i <= 1:
        total = total + i
        i = i + 1

print(total)
