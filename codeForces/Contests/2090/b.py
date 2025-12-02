t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    g = [list(map(int,input().split())) for i in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            pass