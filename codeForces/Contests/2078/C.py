#UNSOLVED
t = int(input())
def solve():
    n = int(input())
    b = list(map(int,input().split()))
    b.sort()
    s = sum(b)
    for i in range(2*n):
        v = s - b[i]
        if (v % 2 == 0):
            m = v // 2
            if m in b:
                b.remove(m)
                return list(b + [m])

for _ in range(t):
    print(*solve())