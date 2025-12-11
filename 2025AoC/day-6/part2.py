values = []
with open('data', 'r') as data:
    for val in list(data.readline()):
        values.append([val])

    for line in list(data.readlines()):
        for idx, val in enumerate(line):
            values[idx].append(val)

col_data = []
for idx in range(len(values)):
    val = ''
    for j in range(len(values[idx])):
        val += values[idx][j]
    col_data.append(val)

cleaned_data = []
curr = []
for vec in col_data:
    if vec.strip() == '':
        if curr:
            cleaned_data.append(curr)
        curr = []
    else:
        curr.append(vec)
if curr:
    cleaned_data.append(curr)

total = 0
for r in cleaned_data:
    symbol = r[0][-1]
    temp = int(r[0][:-1])
    vals = list(map(int,r[1:]))
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