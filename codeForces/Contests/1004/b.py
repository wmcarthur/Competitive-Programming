t = int(input())
for _ in range(t):
    stack = []
    word = input()
    for char in word:
        if stack and stack[-1] == '.':
            if len(stack) > 1:
                stack.pop()
                stack[-1] = '.'
        elif stack and (stack[-1] == char or stack[-1] == '.'):
            stack.pop()
            if stack:
                stack.append(stack[-1])
            else:
                stack.append('.')
        else:
            stack.append(char)
    l = len(stack)
    for i in range(l-1, 0, -1):
        if stack and stack[i] == '.':
            l -= 1
            stack[i - 1] = '.'
            stack.pop(i)
        elif stack and stack[i] == stack[i-1]:
            stack[i-1] = '.'
            l -= 1
            stack.pop(i)
    print(l)