import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    total = 0
    curr = 0
    l = 0
    r = n - 1

    easy = True
    while easy and l <= r:
        if a[l] > 0:
            total += a[l]
            l += 1
        elif a[r] < 0:
            total -= a[r]
            r -= 1
        else:
            easy = False
    if easy:
        print(total)
        continue

    # for i in range(l, r + 1):

    lSum = 0
    rSum = 0
    lStop = False
    rStop = False
    for i in range(r, l -1, -1):
        # print(curr)
        if not rStop:
            if a[i] > 0:
                rSum += a[i]
            elif a[i] < 0:
                
                rStop = True
        if not lStop:
            if a[r-i] < 0:
                lSum -= a[r-i]
            else:
                lStop = True
        if lStop and rStop:
            total += max(lSum, rSum)
            break

    print(total)

    # posSum = 0
    # negSum = 0
    # for i in range(l, r + 1, 1):
    #     if a[i] > 0:
    #         posSum += a[i]
    #     if a[r-i] < 0:
    #         negSum -= a[r-i]
    # print(max(posSum, negSum))

    # # print(l, r)
    # # print(a[l:r])
