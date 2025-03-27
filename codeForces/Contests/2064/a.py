t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    last = 0
    count = 0
    for i in range(len(s)):
        if int(s[i]) == 0 and last == 1:
            count += 1
            last = 0
        elif int(s[i]) == 0:
            continue
        elif int(s[i]) == 1 and last == 0:
            count += 1
            last = 1
        else:
            continue
    print(count)