ticket = input("Enter ticket number: ")

a = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
b = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

if a == b:
    print("YES")
else:
    print("NO")
