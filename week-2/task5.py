allowed = set("ABCEHKMOPTX Y".replace(" ", ""))
n = int(input().strip())

for _ in range(n):
    s = input().strip()
    ok = True

    if len(s) != 6:
        ok = False
    else:
        if s[0] not in allowed:
            ok = False
        if not (s[1].isdigit() and s[2].isdigit() and s[3].isdigit()):
            ok = False
        if s[4] not in allowed or s[5] not in allowed:
            ok = False

    print("Yes" if ok else "No")
