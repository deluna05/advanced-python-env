s1 = int(input("Salary 1: "))
s2 = int(input("Salary 2: "))
s3 = int(input("Salary 3: "))

mx = s1
if s2 > mx:
    mx = s2
if s3 > mx:
    mx = s3

mn = s1
if s2 < mn:
    mn = s2
if s3 < mn:
    mn = s3

print("difference =", mx - mn)
