import math
def find_distance(points, a, b, c, x):
    y = -1 * (c + a*x) / b
    dist = 0
    for i in points:
        dist += math.sqrt((x - i[0])**2 + (y - i[1])**2)
    return dist

def find_optimal_distance(points, a, b, c):
    low = -1000000
    high = 1000000
    while (high - low) > 0.0000001:
        m1 = high - (high - low)/3
        m2 = low + (high - low)/3
        d1 = find_distance(points, a, b, c, m1)
        d2 = find_distance(points, a, b, c, m2)
        if d1 > d2:
            high = m1
        else:
            low = m2
    return find_distance(points, a, b, c, (high + low)/2)

for _ in range(int(input())):
    n = int(input())
    a, b, c = list(map(int, input().split()))
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    print(round(find_optimal_distance(points, a, b, c), 6))
