from Point import Point2D

p1 = Point2D(-1, 2)
p2 = Point2D(3, -6)

''''
         p2
        /|
     n / |
      /__|
   m /|
    / |
   /  |
p1/___|

'''
# Using triangle simetry M/N = (m.x - p1.x)/(p2.x - m.x)
# M(p2.x - m.x) = N(m.x - p1.x)
# M.p2.x -M.m.x = N.m.x - N.p1.x
# Mp2.x + Np1.x = (M + N).x
# x = (M.p2.x + N.p1.x) / (M + N)
# and we do the same thing for Y
# y = (M.p2.y + N.p1.y) / (M + N)

def sectionPoint(p1, p2, m, n):
    x = (p1.x * m + p2.y * n) * m / (m + n)
    y = (p1.y * m + p2.y * n) * m / (m + n)
    return Point2D(x, y)