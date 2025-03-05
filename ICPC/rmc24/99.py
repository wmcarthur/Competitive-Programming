n = int(input())

excess = n % 100
if excess < 49:
    n -= (excess + 1)
else:
    n += (99 - excess)

if n < 0:
    print(99)
elif n > 10000:
    print(9999)
else:
    print(n)
