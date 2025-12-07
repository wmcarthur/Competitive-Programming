line = input().strip().split()
data = []
for val in line:
    data.append([int(val)])

while True:
    try:
        line = input().strip().split()
    except:
        
        break
    
    for idx, val in enumerate(line):
        data[idx].append(val)

total = 0
for r in data:
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