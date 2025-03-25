t = int(input())
for _ in range(t):
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a = sorted(a, reverse=True)
    count = 0
    p = 0
    for num in a:
        p += 1
        if p*num >= x:
            count += 1
            p = 0
    print(count)
