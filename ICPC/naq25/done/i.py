n = int(input())
a = list(map(int, input().split()))
s = sorted(list(map(int, input().split())))
maxBonus = a.index(max(a)) #SLOW
if n == 1:
    print(float(s[0] + a[0]))
else:
    p = 1.0
    total = s[-1]
    maxVal = float(total + a[int(p)-1]) / p
    for i in range(n-2, n-maxBonus-2, -1):
        tempTotal = total + s[i]
        avg = (tempTotal + a[int(p)]) / (p+1)
        maxVal = max(avg, maxVal)
        total = tempTotal
        p += 1
    print(maxVal)