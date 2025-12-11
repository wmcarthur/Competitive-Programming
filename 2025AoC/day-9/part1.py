def calc_area(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

data = []
points = []
with open('data', 'r') as data:
    points = [tuple(map(int, point.split(','))) for point in data.readlines()]

n = len(points)
max_val = 0
for idx1 in range(n):
    for idx2 in range(idx1+1, n):
        val = calc_area(points[idx1], points[idx2])
        max_val = max(max_val, val)
print(max_val)