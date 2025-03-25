t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    d = k//n
    if k%n != 0: d += 1
    e = m - d
    if e == 0:
        print(m)
        continue
    elif e >= m // 2:
        print(1)
        continue
    else:
        if e%2 == 1:
            e -= 1
            e = e // 2
            m = m // 2
        count = (m-e)//(e+1)
        if (m-e)%(e+1) != 0: count += 1
        print(count)
