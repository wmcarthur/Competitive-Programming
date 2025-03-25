n,m = map(int,input().split())
g = [[0 for i in range(m)] for j in range(n)]
a = list(map(int,input().split()))
b = list(map(int,input().split()))
g[0] = b
for val in b: a[0] = a[0]^val
b = [0 for _ in range(len(b))]
for i in range(1,n):
    val = a[i]
    g[i][0] = val
    b[0] = b[0]^val
g[0][0] = g[0][0]^a[0]
# b[0] = b[0]^g[0][0]
b[0] = b[0]^a[0]
if b[0] != 0:
    print("NO")
else:
    print("YES")
    for row in g:
        print(*row)