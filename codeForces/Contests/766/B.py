t = int(input())
# def getAdj(grid, r, c):


def solve():
    n,m = map(int, input().split())
    grid = [[0 for a in range(m)]for b in range(n)]
    numCenter = 1
    if n%2 == 0: numCenter *= 2
    if m%2 == 0: numCenter *= 2
    #Get first val
    val = (0 - n//2) + (0 - m//2)
    answer = [val for __ in range(numCenter)]
    # for k in range(n*m - 1):
    #     pass


for _ in range(t):
    solve()