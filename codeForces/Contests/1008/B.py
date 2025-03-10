#SOLVED
t = int(input())
def solve():
    n, k = map(int, input().split())
    
    if k % 2 == 1:
        a = [n for i in range(n-1)]
        a.append(n-1)
    else:
        a = [n-1 for i in range(n)]
        a[-2] += 1
    return a
            
    
for _ in range(t):
    print(*solve())