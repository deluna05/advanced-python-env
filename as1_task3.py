A = float(input("Enter number with 2 decimals: "))

integer_part = int(A)
fractional_part = int((A - integer_part) * 100)

new_number = fractional_part + integer_part / 100

print("{:.2f}".format(new_number))
