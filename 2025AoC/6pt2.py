line = list(input())
data = []
for val in line:
    data.append([val])

while True:
    try:
        line = list(input())
    except:
        
        break
    
    for idx, val in enumerate(line):
        data[idx].append(val)
print(data)
col_data = []
for idx in range(len(data)):
    val = ''
    for j in range(len(data[idx])):
        val += data[idx][j]
        print(val)
    col_data.append(val)
print(col_data)

cleaned_data = []
curr = []
for vec in col_data:
    if vec.strip() == '':
        cleaned_data.append(curr)
        curr = []
    else:
        curr.append(vec)
        print()
cleaned_data.append(curr)
print(cleaned_data)
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
    print(temp)
    total += temp
print(total)