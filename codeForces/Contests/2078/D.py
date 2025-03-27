t = int(input())
for _ in range(t):
    n = int(input())
    g = []
    l = 1
    r = 1
    for i in range(n):
        g.append(input().split())
        g[i][1] = int(g[i][1])
        g[i][3] = int(g[i][3])
    best = [0 for i in range(n+1)]
    for i in range(n-1, -1, -1):
        if g[i][0] == 'x' and g[i][2] == '+': best[i] = 0
        elif g[i][0] == '+' and g[i][2] == 'x': best[i] = 1
        elif g[i][0] == 'x' and g[i][2] == 'x':
            if g[i][1] < g[i][3]: best[i] = 1 
            elif g[i][1] == g[i][3]: best[i] = best[i+1]
        else:
            best[i] = best[i+1]
    for i in range(n):
        p = 0
        if g[i][0] == '+': p += g[i][1]
        else: p += (g[i][1]-1) * l
        if g[i][2] == '+': p += g[i][3]
        else: p += (g[i][3]-1) * r
        if best[i+1]:
            r += p
        else:
            l += p
        # print('l', l, 'r', r)
    # print(*best)
    print(l+r)

    

