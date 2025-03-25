t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = 1
        else:
            d[a[i]] += 1
        if 3 in d and 1 in d and 0 in d and 2 in d and 5 in d:
            if d[3] >= 1 and d[1] >= 1 and d[0] >= 3 and d[2] >= 2 and d[5] >= 1:
                print(i+1)
                break
            elif i == n-1:
                print(0)
                break
        elif i == n-1:
            print(0)
            break
