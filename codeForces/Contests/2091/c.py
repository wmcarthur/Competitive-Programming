t = int(input())
for _ in range(t):
    n = int(input())
    if n%2 == 0:
        print(-1)
        continue
    a = []
    for i in range(n-1, -1, -1):
        a.append(i+1)
    print(*a)