t = int(input())

def run():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))

    a[0] = min(a[0], min([b[j] - a[0] for j in range(m)]))

    def bs(target, idx):
        l = 0
        r = m
        p = m // 2
        while r > l:
            v = b[p] - a[idx]
            if v == target:
                return v
            if v > target:
                r = p - 1
                p = (l + r) // 2
                continue
            l = p + 1
            p = (l + r) // 2
        if b[p] - a[idx] < target:
            p += 1
        return b[p] - a[idx]

    for i in range(1, n):
        target = a[i-1]
        val = a[i]
        if a[i] >= target:
            a[i] = min(a[i], bs(target, i))
        else:
            a[i] = bs(target, i)
        # for j in range(m):
        #     newVal = b[j] - a[i]
        #     if a[i] < target:
        #         a[i] = newVal
        #     if newVal >= target:
        #         a[i] = min(val, newVal)
        #         break
    for i in range(1, n):
        if a[i] < a[i-1]:
            return False
    return True
                
for _ in range(t):
    if run():
        print("YES")
    else:
        print("NO")