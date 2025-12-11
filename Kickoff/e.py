t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    low = 0
    high = 0
    l = 1
    r = 1
    curr = 0
    for i in range(n-1):
        val = a[i]
        curr += val
        if curr < low:
            l = i + 2
            low = curr
        elif curr >= high:
            r = i + 2
            high = curr

    print(l, r)