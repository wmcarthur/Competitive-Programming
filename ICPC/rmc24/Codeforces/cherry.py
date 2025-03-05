t = int(input())
for i in range(t):
    n = int(input())
    line = list(map(int, input().split()))
    maxScore = 0
    for j in range(0, n - 1):
        score = line[j] * line[j + 1]
        maxScore = max(maxScore, score)
    print(maxScore)
    
