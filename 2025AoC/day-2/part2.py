with open('data', 'r') as data:
    ranges1 = data.readline().strip().split(',')

ranges = []
for r in ranges1:
    start, end = r.split('-')
    if len(start) == len(end):
        ranges.append(r)
    else:
        mid = 10**(len(end)-1)
        ranges.append(start+'-'+str(mid-1))
        ranges.append(str(mid)+'-'+end)
        
total = 0
used = set()
for rng in ranges:
    start, end = rng.split('-')
    l = int(start)
    r = int(end)
    if len(start) % 2 == 1 and len(end) % 2 == 1:
        pass
    
    f = start[0]
    
    for length in range(1, len(end)):
        if len(end) % length != 0:
            continue
        try:
            f = start[:length]
        except:
            f = 10**(length-1)
        
        valid = True
        while valid:
            val = f
            for i in range(len(end)//length - 1):
                val += f
            if val in used:
                f = str(int(f)+1)
                continue
            if int(val) >= l and int(val) <= r:
                total += int(val)
                used.add(val)
            elif int(val) > r:
                valid = False
            f = str(int(f)+1)
        
print(total)