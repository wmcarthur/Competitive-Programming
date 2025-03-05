n = int(input())
s = input()
t = list(s)
l = 0
r = 0
c = 0
for i in s:
    if i == '(':
        l += 1
        c += 1
    else:
        r += 1
        c -= 1
    if c == -2:
        print("No")
        break
else:
    while s.find("()") != -1:
        s = s.replace('()', '')
 
    if len(s) % 2 == 1 or len(s) > 2:
        print("No")
    else:
        s = list(s)
        if len(s) > 1 and s[0] == s[1]:
            print("No")
        else:
            print("Yes")