t = int(input())

def run():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))

    a[0] = min(a[0], min([b[j] - a[0] for j in range(m)]))
    for i in range(1, n):
        j = 0
        target = a[i-1]
        nextVal = -float('inf')
        while (nextVal < target and j < m):
            nextVal = b[j] - a[i]
            j += 1
        if a[i] >= target:
            a[i] = min(a[i], nextVal)
        else:
            a[i] = nextVal
        if a[i] < target:
            return False
    for i in range(1, n):
        if a[i] < a[i-1]:
            return False
    return True

for _ in range(t):
    if run():
        print("YES")
    else:
        print("NO")