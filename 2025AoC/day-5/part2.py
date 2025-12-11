ranges = []
ingredients = []
switch = True
with open('data', 'r') as data:
    for line in data.readlines():
        if line.strip() == '':
            switch = False
            continue
        if switch:
            ranges.append(list(map(int, line.strip().split('-'))))
        else:
            ingredients.append(int(line.strip()))
    lines = [line.strip() for line in data.readline()]

total = 0
for ingredient in ingredients:
    for r in ranges:
        if ingredient >= r[0] and ingredient <= r[1]:
            total += 1
            break
print("Part 1:", total)

orderedR = sorted(ranges, key=lambda x: x[0])
def merge_ranges(ranges):
    ranges = sorted(ranges)
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:  # overlap
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged

def count_unique_values(ranges):
    merged = merge_ranges(ranges)
    total = 0
    for a, b in merged:
        total += b - a + 1
    return total

ranges = orderedR
print("Part 2:", count_unique_values(ranges))