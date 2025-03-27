t = int(input())
def solve():
    n, x = map(int, input().split())
    s = []
    for i in range(31, -1, -1):
        if (x & (1 << i)) != 0:
            s.append(1 << i)
    #find first missing min
    min = 0
    for i in range(len(s) + 1):
        # print(2**i)
        if 2**i not in s:
            min = 2**i
            break
    # print(min)
    # print(s)
    l = len(s)
    i = 0
    for i in range(min):
        if i not in s:
            s.append(i)
    s = sorted(s)
    # print(s)
    while len(s) > n:
        v = s.pop()
        s[-1] |= v
    
    while len(s) < n:
        s.append(0)

    return s

    

for _ in range(t):
    
    print(*solve())