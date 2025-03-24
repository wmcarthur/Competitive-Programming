t = int(input())
# def getAdj(grid, r, c):


def solve():
    n,m = map(int, input().split())
    grid = [[0 for a in range(m)]for b in range(n)]
    numCenter = 1
    if n%2 == 0: numCenter *= 2
    if m%2 == 0: numCenter *= 2
    #Get first val
    dist = (0 - n//2) + (0 - m//2)
    answer = [dist for __ in range(numCenter)]
    # for k in range(n*m - 1):
    #     pass
    seen = numCenter
    if numCenter == 1:
        k = 1
        while seen < (n * m):
            newSeen = min(n, 2*k + 1) * 2 + min(m, 2*k + 1) * 2 - 4
            for _ in range(newSeen):
                answer.append(dist + k)
            k += 1
            seen += newSeen
    return answer



for _ in range(t):
    print(*solve())