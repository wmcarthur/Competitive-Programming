ranges = []
ingredients = []
l = []
f = True
while True:
    try:
        line = input().strip()
    except:
        break
    
    if line == '':
        ranges = l
        l = []
        f = False
        continue
    if f:
        l.append(list(map(int, line.split('-'))))
    else:
        l.append(int(line))
ingredients = l
# print(ranges)
# print(ingredients)
total = 0

for ingredient in ingredients:
    for r in ranges:
        if ingredient >= r[0] and ingredient <= r[1]:
            total += 1
            break
print(total)

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
print(count_unique_values(ranges))

        
# print(len(val))