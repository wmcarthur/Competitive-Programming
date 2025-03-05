t = int(input())
def solve():
    n = int(input()) #len(s)
    s = list(input())
    dash = 0
    under = 0
    sum = 0
    for char in s:
        if char == '-':
            dash += 1
        else:
            under += 1
    if n < 3 or dash < 2 or under < 1:
        return 0
    if dash % 2 == 1:
        sum = (dash // 2) * (dash // 2 + 1) * under
    else:
        sum = (dash // 2) * (dash // 2) * under
    return sum

for _ in range(t):
    print(solve())