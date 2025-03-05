t = int(input())
strings = []
for i in range(t):
    strings.append(input())

for i in range(t):
    case = True
    s = strings[i]
    a = []
    s += s[0]
    curr = ''
    nCount = 0
    for j in range(1, len(s)):
        curr = s[j]
        if curr == 'E':
            nCount += 1
    # if len(s) == 2:
    #     if s[0] != s[1]:
    #         case = False
    if nCount == 1:
        case = False
    if case:
        print("YES")
    else:
        print("NO")
