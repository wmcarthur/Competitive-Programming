t = int(input())
def solve():
    n, k, p = map(int,input().split())
    sum = 0
    num = 0
    count = 0
    while num < n and sum != k:
        # print(sum)
        if sum < k:
            sum += min(p, k - sum)
        else:
            sum += max(-p, k - sum)
        num += 1
        count += 1
    if sum == k:
        return count
    if n == 0 and k != 0:
        return -1
    if num == n:
        return -1
    return count

for _ in range(t):
    print(solve())
