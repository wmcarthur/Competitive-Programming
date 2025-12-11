from math import dist
lines = []
with open('data', 'r') as data:
    lines = data.readlines()
points = [tuple(map(int, item.split(','))) for item in lines]
n = 1000

distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distances.append((dist(points[i], points[j]), points[i], points[j]))

distances.sort()
distances = distances[:n]
distances = sorted(distances, key=lambda x: x[2])
def merge_groups(idx1, idx2, g):
    group2 = g.pop(idx2)
    group1 = g.pop(idx1)
    combined = [group1 + group2] + g
    return combined

groups = []
for shortest_point in distances:
    found = set()
    for group_idx, group in enumerate(groups):
        for picked_pair in group:
            if shortest_point[1] in picked_pair or shortest_point[2] in picked_pair:
                groups[group_idx].append(shortest_point)
                found.add(group_idx)
                break
    if len(found) == 0:
        groups.append([shortest_point])
    elif len(found) == 2:
        found_list = sorted(list(found))
        groups = merge_groups(found_list[0], found_list[1], groups)

sizes = []
for group in groups:
    s = set()
    for point in group:
        s.add(point[1])
        s.add(point[2])
    sizes.append(len(s))

sizes = sorted(sizes, reverse=True)
print(sizes[0]*sizes[1]*sizes[2])
