a = float(input("First number: "))
op = input("Operation (+, -, *, /): ")
b = float(input("Second number: "))

if op == "/":
    b == 0 and print("Error: division by zero is impossible")
    b != 0 and print(a, "/", b, "=", a / b)
elif op == "+":
    print(a, "+", b, "=", a + b)
elif op == "-":
    print(a, "-", b, "=", a - b)
elif op == "*":
    print(a, "*", b, "=", a * b)
else:
    print("Unknown operation")
