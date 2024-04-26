import math
points = [(1, 3), (2, 8), (7, 18), (15, 23)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
distances = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)
print(f"The minimum distance: {min_distance:.2f}")
