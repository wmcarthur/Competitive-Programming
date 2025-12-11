values = []
with open('data', 'r') as data:
    for val in data.readline().split():
        values.append([int(val)])

    for line in data.readlines():
        for idx, val in enumerate(line.strip().split()):
            values[idx].append(val)

total = 0
for r in values:
    temp = r[0]
    symbol = r[-1]
    vals = list(map(int,r[1:-1]))
    for val in vals:
        if symbol == '+':
            temp += val
        elif symbol == '-':
            temp -= val
        elif symbol == '*':
            temp *= val
        elif symbol == '/':
            temp /= val
    total += temp
print(total)