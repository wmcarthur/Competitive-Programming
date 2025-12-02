t = int(input())
for _ in range(t):
    x,y,a = map(int, input().split())
    if a % (x+y) < x: print("NO")
    else: print("YES")