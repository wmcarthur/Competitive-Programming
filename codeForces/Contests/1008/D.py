#TLE/MLE
t = int(input())
def solve():
    found = {}
    def dp(i, l, r): #Depth, left, right
        if i >= n:
            return l+r
        if (i,l,r) in found:
            return found[(i,l,r)]
        p = 0
        if gates[i][0] == '+': p += gates[i][1]
        else: p += (gates[i][1]-1) * l
        if gates[i][2] == '+': p += gates[i][3]
        else: p += (gates[i][3]-1) * r
        # print("People:", p)
        half = p//2
        rem = p - half
        bestVal = max(dp(i+1, l+p, r), dp(i+1, l, r+p), dp(i+1, l+half, r+rem), dp(i+1, l+rem, r+half))
        found[(i,l,r)] = bestVal
        return bestVal
    n = int(input())
    gates = []
    for i in range(n):
        gates.append(input().split())
        gates[i][1] = int(gates[i][1])
        gates[i][3] = int(gates[i][3])
    return dp(0,1,1)


for _ in range(t):
    print(solve())