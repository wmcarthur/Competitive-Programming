t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = sorted(a)
    l = 0
    r = n - 1
    out = []

    for i in range(n):
        word = input()
        if word == "max":
            out.append(a[r])
            r -= 1
        else:
            out.append(a[l])
            l += 1

    print(*out)
