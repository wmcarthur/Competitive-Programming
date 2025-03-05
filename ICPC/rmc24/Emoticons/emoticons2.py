string = input()
chars = []
for s in string:
    chars.append(s)
emojis = [":-)",":-(",";-)","xD","^_^","-_-","^o^",'^^;',"(..)",":)"]
visible = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
max = len(string)
min = max
newMin = min
maxStr = 0
for c in visible:
    for w in chars:
        l = 0
        i = 0
        newMin = max
        newStr = string.replace(w,c)
        while i < len(newStr):
            for emoji in emojis:
                if newStr[i:].startswith(emoji):
                    i += len(emoji)
                    l += 1
                    newMin -= (len(emoji) - 1)
                    break
            else:
                i += 1
                l += 1
        if (newMin < min):
        # print(newStr)
            min = newMin
        if (l > maxStr):
            maxStr = l

print(min, maxStr)