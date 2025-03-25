t = int(input())
def solve():
    n,k = map(int,input().split())
    s = list(input())
    if n < 2:
        return False
    if k == 0:
        count = 0
        for i in range(n):
            if i > n - i:
                if count < i-1:
                    return True
                return False
            elif s[i] == s[n-i-1]:
                count += 1
            else:
                return not (s[i] > s[n-i-1])
    for i in range(n):
        if s[i] != s[0]:
            return True
    return False

for _ in range(t):
    if solve(): print("YES")
    else: print("NO")