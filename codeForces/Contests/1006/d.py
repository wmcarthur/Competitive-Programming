t = int(input())
def solve():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    lv = -1
    rv = -1
    for i in range(1, n):
        if a[i] < a[i-1]:
            lv = i - 1
            break
    for i in range(n-2, -1, -1):
        if a[i+1] < a[i]:
            rv = i-1
            break
    rv2 = -1
    for i in range(n-2, -1, -1):
        if a[i+1] <= a[lv-1]:
            rv2 = i+1
            break
    # if rv != -1 and rv2 != -1:
    #     if a[rv-1] > a[rv2-1]: 
    #         rv = rv2
    if lv == -1 and rv == -1:
        lv = 0; rv = 0
    else:
        if lv == -1: lv = 0
        if rv == -1: rv = n - 1
    lv += 1; rv += 1

    if a[n-1] < a[lv-1]:
        return [lv, n]
    return [lv,rv]

for _ in range(t):
    print(*solve())