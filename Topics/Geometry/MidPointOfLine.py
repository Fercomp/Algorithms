from Point import Point2D

# Using tuples 
p1 = (-1, 2)
p2 = (3, -6)
def midPointTuples(p1, p2):
    x = (p1[0] + p2[0]) / 2
    y = (p1[1] + p2[1]) / 2
    return (x, y)

# Using the Point2D
p3 = Point2D(-1, 2)
p4 = Point2D(3, -6)
def midPoint(p1: Point2D, p2: Point2D) -> Point2D:
    return (p1 + p2) / 2

print(midPointTuples(p1, p2)) # (1, -2)
print(midPoint(p3, p4))       # (1, -2)