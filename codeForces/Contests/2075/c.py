t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    count = 0
    # c = [0 for i in range(n+1)]
    for i in range(m):
        a[i] = min(a[i], n-1)
    # ps = 0
    # for i in range(n):
    #     if c[i] > 0:
    #         count += c[i] * ps
    #         ps += c[i]
    s = sum(a)
    count = (m-1)*s - n**2 - 1


    # for i in range(m):
    #     f = a[i]
    #     for j in range(i+1, m):
    #         s = a[j]
    #         v = (min(f, n-1) + min(s, n-1) - n + 1)
    #         if v > 0:
    #             count += v

    print(count)
    
