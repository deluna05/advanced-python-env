month = input()

if month.isdigit():
    month = int(month)

    if month < 1 or month > 12:
        print("not real month")

    else:
        if month == 1:
            print("You were born in January. White snow fell outside the window.")
        if month == 2:
            print("You were born in February. White snow fell outside the window.")
        if month == 3:
            print("You were born in March. Birds sang beautiful songs.")
        if month == 4:
            print("You were born in April. Birds sang beautiful songs.")
        if month == 5:
            print("You were born in May. Birds sang beautiful songs.")
        if month == 6:
            print("You were born in June. The sun shone brighter than ever.")
        if month == 7:
            print("You were born in July. The sun shone brighter than ever.")
        if month == 8:
            print("You were born in August. The sun shone brighter than ever.")
        if month == 9:
            print("You were born in September. The harvest was incredible.")
        if month == 10:
            print("You were born in October. The harvest was incredible.")
        if month == 11:
            print("You were born in November. The harvest was incredible.")
        if month == 12:
            print("You were born in December. White snow fell outside the window.")

else:
    print("You need to enter the real number of the month")