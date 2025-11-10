# Here we won't use the line equation used in scholl y = ax + b
# this can't deal with vertical lines, because a = y2-y1/x2-x1,
# and if is vertical x2-x1 is zero and we can't divide by zero.
# So instead of that we will use the general form ax + by = c
# if line is horizontal a = 0, and if line is vertical b = 0

# So if we are given two points p1 and p2 we can do the following system
# a.p1.x + b.p1.y = c
# a.p2.x + b.p2.y = c

# a(p1.x - p2.x) = b(p1.y - p2.y)
# a = (p1.y - p2.y)
# b = (p1.x - p2.x)
# c = a.p1.x + b.p1.y = a.p2.x + b.p2.y

from Point import Point2D

def line(p1: Point2D, p2: Point2D):
    a = p2.y - p1.y
    b = p1.x - p2.x
    c = a * p1.x + b * p1.y
    return a, b, c

class Line:
    def __init__(self, p1: Point2D, p2: Point2D):
        self.a = p2.y - p1.y
        self.b = p1.x - p2.x
        self.c = a * p1.x + b * p1.y