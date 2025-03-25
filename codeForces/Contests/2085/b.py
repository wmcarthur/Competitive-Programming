t = int(input())
def mex(nums):
    seen = set()
    for num in nums:
        if num >= 0:
            seen.add(num)

    mex = 0
    while mex in seen:
        mex += 1
    return mex

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    sol = []
    k = 0
    while n > 1:
        k += 1
        # print(a)
        if not a.__contains__(0):
            sol.append((1, n))
            # print(sol)
            print(k)
            return sol
        else:
            l = a.index(0)
            r = l + 2
            if l == n-1:
                l -= 1
                r -=1
            a = a[0:l] + [mex(a[l:r])] + a[r:]
            n = len(a)
            sol.append((l+1,r))
    # print(sol)    
    print(k) 
    return sol




for _ in range(t):
    s = solve()
    for coord in s:
        print(*coord)