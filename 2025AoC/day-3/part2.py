with open('data', 'r') as data:
    banks = [list(bank.strip()) for bank in data.readlines()]

total = 0
for bank in banks:
    vals = bank[-12:]
    for i in range(len(bank)-13, -1, -1):
        head = 0
        val = bank[i]
        while head < 12 and val >= vals[head]:
            temp = vals[head]
            vals[head] = val
            val = temp
            head += 1
    total += int(''.join(vals))
    
print(total)