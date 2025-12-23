def all_eq(lst):
    mx = 0
    for s in lst:
        if len(s) > mx:
            mx = len(s)

    res = []
    for s in lst:
        res.append(s + "_" * (mx - len(s)))
    return res


lst = input().split()
print(all_eq(lst))
