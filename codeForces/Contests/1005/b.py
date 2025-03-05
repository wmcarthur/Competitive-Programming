t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    loc = {}
    pos = set()
    count = 0
    for i in range(n):
        if a[i] in loc:
            pos.add(loc[a[i]])
            pos.add(i)
        else:
            loc[a[i]] = i
    count = len(pos)
    if n == count:
        print(0)
    elif not count:
        print(1, n)
    else:
        l = 1
        #Find unused indices
        pos = sorted(pos)
        diff = pos[0]
        max = n - count - diff

        for j in range(1, count):
            if diff >= max:
                break
            gap = pos[j] - pos[j-1] - 1
            if gap > diff:
                diff = gap
                l = pos[j-1] + 2
                max -= diff
        if n - pos[-1] - 1 > diff:
            diff = n - pos[-1] - 1
            l = pos[-1] + 2
        print(l, l + diff - 1)