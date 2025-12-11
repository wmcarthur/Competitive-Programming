with open('data', 'r') as data:
    lines = [line.strip() for line in data.readlines()]

pos = 50
count = 0
for line in lines:
        
    dir = line[0]
    dist = int(line[1:])

    for _ in range(dist):
        if dir == 'L':
            pos -= 1
            if pos < 0:
                pos = 99
        elif dir == 'R':
            pos += 1
            if pos > 99:
                pos = 0
                     
        if pos == 0:
            count += 1

print(count)
