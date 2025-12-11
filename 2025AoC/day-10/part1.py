from heapq import heappush, heappop
def switch(c):
    if c == '.': return '#'
    return '.'

def press_button(button, machine):
    machine = list(machine)
    for idx in button:
        machine[idx] = switch(machine[idx])
    return tuple(machine)

machines = []
with open('data', 'r') as data:
    for line in data.readlines():
        diagram = tuple(line[1:line.index(']')])
        buttons = ')' + line[line.index(']')+1 : line.index('{')] + '('
        buttons = (buttons.split(") ("))[1:-1]
        buttons = [list(map(int, button.split(','))) for button in buttons]
        machines.append((diagram, buttons))

total = 0
for machine in machines:
    target_state, buttons = machine
    seen = set()
    q = [(0, tuple(['.' for _ in range(len(target_state))]))]
    while q:
        cost, curr_machine = heappop(q)
        
        if curr_machine in seen:
            continue
        seen.add(curr_machine)

        if curr_machine == target_state:
            total += cost
            print("Found:", cost)
            break
        
        for button in buttons:
            pressed_machine = press_button(button, curr_machine)
            
            if pressed_machine in seen:
                continue
            
            heappush(q, (cost + 1, pressed_machine))

print(total)