t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if k == 1:
        if n == 2:
            cost = sum(a)
        else:
            cost = 0
            cost += max(a[0], a[-1])
            cost += max(max(a[1:-1]), min(a[0], a[-1]))
            
    else:
        a = sorted(a)
        cost = sum(a[-(k+1):])
    print(cost)