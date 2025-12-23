eq = input().strip()

a = eq[0]
op = eq[1]
b = eq[2]
c = eq[4]

if a == "x":
    B = int(b)
    C = int(c)
    if op == "+":
        print(C - B)
    else:
        print(C + B)

elif b == "x":
    A = int(a)
    C = int(c)
    if op == "+":
        print(C - A)
    else:
        print(A - C)

else:
    A = int(a)
    B = int(b)
    if op == "+":
        print(A + B)
    else:
        print(A - B)
