# SOLVED
t = int(input())
def solve():
    n, x = map(int, input().split())
    a = list(map(int,input().split()))
    s = sum(a)
    if s / n == x: return True
    return False
    
for _ in range(t):
    if solve():
        print("YES")
    else:
        print("NO")