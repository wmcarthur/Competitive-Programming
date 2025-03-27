t = int(input())

def run():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i in range(n):
        c.append(b[0] - a[i])
        a[0] = min(a[0], c[0])
    for i in range(1, n):
        val = a[i]
        a[i] = min(a[i], c[i])
        if a[i] < a[i-1]:
            a[i] = max(val, c[i])
    # for i in range(1, n, 1):
    #     if a[i] < a[i-1]:
    #         if (c[i-1] < a[i-1] and c[i-1] <= a[i]):
    #             a[i-1] = c[i-1]
    #         elif ():
    for i in range(1, n):
        if a[i] < a[i-1]:
            return False
    return True
                
for _ in range(t):
    if run():
        print("YES")
    else:
        print("NO")