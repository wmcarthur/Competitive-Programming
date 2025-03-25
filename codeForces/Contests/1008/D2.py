#Bottom-up solution for problem D
t = int(input())
def add(g,i,j,r):
    val = g[i][j]
    if r:



for _ in range(t):
    n = int(input())
    gates = []
    for i in range(n):
        gates.append(input().split())
        gates[i][1] = int(gates[i][1])
        gates[i][3] = int(gates[i][3])
    g = [[0 for __ in range(n)] for ___ in range(n)]
    g[0][0] = (1,1)
    for i in range(n):
        for j in range(n):
            if i + j > n:
                break
            if i == 0 and j == 0:
                continue
            if i == 0:
                val = g[i][j-1]
                g[i][j] = val
            elif j == 0:
                pass
            else:
                pass