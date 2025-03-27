t = int(input())

def run():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))
    c = [[a[_]] for _ in range(n)]
    for j in range(m):
        c[0].append(b[j] - a[0])
    a[0] = min(a[0], min(c[0]))
    for i in range(1, n):
        target = a[i-1]
        val = a[i]
        for j in range(1, m+1):
            c[i].append(b[j - 1] - a[i])
            newVal = c[i][j]
            if c[i][0] < target:
                c[i][0] = newVal
            if newVal >= target:
                c[i][0] = min(c[i][0], newVal)
                break
        a[i] = min(a[i], c[i][0])
        if a[i] < a[i-1]:
            a[i] = max(val, c[i][0])
    for i in range(1, n):
        if a[i] < a[i-1]:
            return False
    return True
                
for _ in range(t):
    if run():
        print("YES")
    else:
        print("NO")