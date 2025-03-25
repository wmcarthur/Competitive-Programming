t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = 0
    if n % 2 == 1:
        a = 1
        n -= k
    if k%2 == 1: k-=1
    if n%k: a += 1
    a += n // k
    print(a)