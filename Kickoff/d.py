t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    s = []
    w = []
    for i in range(n):
        s.append(list(map(int, input().split())))
        w.append(list(map(int, input().split())))
    rankings = []
    for i in range(n):
        t = 0
        p = 0
        l = 0
        for j in range(m):
           if s[i][j] != -1:
               p += 1
               t += s[i][j] + 20 * w[i][j]
               l = max(l, s[i][j])
        
        rankings.append((p, 10000-t, 10000-l, i+1))
    rankings = sorted(rankings, reverse=True)
    # print(rankings)

    clean = [0] * n
    prev = rankings[0]
    clean[prev[3] - 1] = 1
    count = 0
    for i in range(1, n):
        curr = rankings[i]
        if curr[0:3] == prev[0:3]:
            clean[curr[3] - 1] = i - count
            count += 1
        else:
            clean[curr[3] - 1] = i + 1
            count = 0

        prev = curr

    print(*clean)



        