with open('data', 'r') as data:
    banks = [list(bank.strip()) for bank in data.readlines()]

total = 0
for bank in banks:
    best = 0
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            val = int(bank[i]+bank[j])
            best = max(val, best)
    total += best

print(total)