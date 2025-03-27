t = int(input())
def solve():
    n, x = map(int, input().split())
    s = []
    sum = 0

    


    for i in range(31, -1, -1):
        if (x & (1 << i)) != 0:
            s.append(1 << i)

    if len(s) < n:
        s = s + [0 for _ in range(n-i)]

    while len(s) > n:
        v = s.pop()
        s[-1] |= v

    return s    

for _ in range(t):
    print(*solve())