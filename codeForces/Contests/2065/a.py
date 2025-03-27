t = int(input())
for _ in range(t):
    word = list(input())
    word.pop(-1)
    word[len(word) - 1] = 'i'
    print("".join(word))
    