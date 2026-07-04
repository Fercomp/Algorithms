from Point import Point2D
import Math

p1 = Point2D(4, 2)
p2 = Point2D(2, 5)

def slopeOfLine(p1: Point2D, p2: Point2D):
    # The smaller is the difference between p2.x and p1.x the grather
    # is the line slope
    if p2.x - p1.x == 0:
        return Math.inf
    return (p2.y - p1.y) / (p2.x - p1.x)