items = input().split()

freq = {}
for x in items:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print("Purchase frequency:")
for name in freq:
    print(f"{name}: {freq[name]}")

best_item = None
best_count = -1
for name in freq:
    if freq[name] > best_count:
        best_count = freq[name]
        best_item = name

print("Most popular item:", best_item)

once = []
for name in freq:
    if freq[name] == 1:
        once.append(name)

print("Purchased once:", " ".join(once))

sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

print("Sorted by frequency:")
for name, cnt in sorted_items:
    print(name, cnt)
