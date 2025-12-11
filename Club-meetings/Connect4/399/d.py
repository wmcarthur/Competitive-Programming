t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.append(0)
    count = 0
    m = [[] for __ in range(n+1)]
    grouped = []
    for i in range(2*n):
        if i in grouped:
            continue
        if i > 0:
            if m[a[i]] != a[i-1]:
                m[a[i]].append(a[i-1])
            else:
                grouped.append(a[i])
        if i < 2 * n - 1:
            if m[a[i]] != a[i+1]:
                m[a[i]].append(a[i+1])
            else:
                grouped.append(a[i])

    pairs = []
    for i in range(1,n+1):
        print(m[i])
        for val in m[i]:
            if i in m[val]:
                if (i, val) not in pairs and i != val and i not in grouped and val not in grouped:
                    count += 1
                    pairs.append((i, val))
    print(count)
