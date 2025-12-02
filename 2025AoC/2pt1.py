ranges = input().strip().split(',')
total = 0
for range in ranges:
    start, end = range.split('-')
    l = int(start)
    r = int(end)
    if len(start) % 2 == 1 and len(end) % 2 == 1:
        pass
    
    valid = True
    
    # print(start, "-", end)
    if len(start) == 1:
        f = start
    else:
        f = start[:len(start)//2]
    # print(f)
    
    while valid:
        # print(f, type(f))
        val = f+f
        if int(val) >= l and int(val) <= r:
            total += int(val)
        elif int(val) > r:
            valid = False
        f = str(int(f)+1)
        
print(total)