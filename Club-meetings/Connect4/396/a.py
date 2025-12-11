
def solve():
    n = int(input())
    a = list(map(int,input().split()))
    p = a[0]
    c = 1
    for i in range(1, n):
        if a[i] == p:
            c += 1
            if c == 3:
                return True
        else:
            p = a[i]
            c = 1
    return False

if solve():
    print("Yes")
else:
    print("No")
