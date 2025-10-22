from Point import Point2D

p1 = Point2D(-1, 2)
p2 = Point2D(3, -6)

def midPoint(p1, p2):
    x = (p1.x + p2.x) / 2
    y = (p1.y + p2.y) / 2
    return x, y