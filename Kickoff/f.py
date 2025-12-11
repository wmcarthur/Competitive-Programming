t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    n = int(input())
    q = list(map(int, input().split()))

    p = set()
    p.update([a,b,c])
    v = c % a


