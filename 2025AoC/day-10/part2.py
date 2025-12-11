from heapq import heappush, heappop
def switch(c):
    if c == '.': return '#'
    return '.'

def press_button(button, machine, joltage):
    machine = list(machine)
    joltage = list(joltage)
    for idx in button:
        machine[idx] = switch(machine[idx])
        joltage[idx] += 1
    return tuple(machine), tuple(joltage)

machines = []
with open('data', 'r') as data:
    for line in data.readlines():
        diagram = tuple(line[1:line.index(']')])
        buttons = ')' + line[line.index(']')+1 : line.index('{')] + '('
        buttons = (buttons.split(") ("))[1:-1]
        buttons = [list(map(int, button.split(','))) for button in buttons]
        joltage = line[line.index('{')+1 : line.index('}')]
        joltage = tuple(map(int, joltage.strip().split(',')))
        machines.append((diagram, buttons, joltage))
        
total = 0
for machine in machines:
    print(machine)
    target_state, buttons, joltage = machine
    seen = set()
    curr_machine = tuple(['.' for _ in range(len(target_state))])
    curr_jolts =  tuple([0 for _ in range(len(joltage))])
    q = [(0, curr_machine, curr_jolts)]
    while q:
        cost, curr_machine, curr_jolts = heappop(q)
        # print("M",curr_machine, target_state)
        # print("J",curr_jolts, joltage)
        
        if curr_jolts in seen:
            continue
        seen.add(curr_jolts)
        
        overshot = False
        for jolt, max_jolt in zip(curr_jolts, joltage):
            if jolt > max_jolt:
                overshot = True
        if overshot:
            continue

        if curr_jolts == joltage:
            total += cost
            print("Found:", cost)
            break
        
        for button in buttons:
            pressed_machine, pressed_jolts = press_button(button, curr_machine, curr_jolts)
            
            if pressed_jolts in seen:
                continue
            
            heappush(q, (cost + 1, pressed_machine, pressed_jolts))
    else:
        print("No combination found")

print("TOTAL:",total)