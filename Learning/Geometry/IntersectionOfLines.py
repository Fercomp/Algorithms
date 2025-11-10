# We have two lines:
# 1) a1x + b1y = c1
# 2) a2x + b2y = c2
# We have to now solve these 2 equations to find the point of intersection.
# To solve, we multiply 1. by b2 and 2 by b1 This gives us: 
# a1b2x + b1b2y = c1b2 and a2b1x + b2b1y = c2b1 Subtracting these we get\
# (a1b2 - a2b1) x = c1b2 - c2b1 This gives us the value of x. 
# Similarly, we can find the value of y. (x, y) gives us the point of intersection.

from Point import Point2D

def line(p1: Point2D, p2: Point2D):
    a = p2.y - p1.y
    b = p1.x - p2.x
    c = a * p1.x + b * p1.y
    return a, b, c

def intersection_point(A, B, C, D):
    a1, b1, c1 = line(A, B)
    a2, b2, c2 = line(C, D)
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        # As retas são paralelas (ou coincidentes)
        return None
    
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant
    return Point2D(x, y)

A = Point2D(1, 1)
B = Point2D(4, 4)
C = Point2D(1, 8)
D = Point2D(2, 4)
print(intersection_point(A, B, C, D))