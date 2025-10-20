from Point import Point2D
import math

# To avoid precision errors we can use EPS (epslon) variable to know if a result
# is close enoght to the wanted solution
# EPS = 10^-9

# Points are considered 0D objects

# The modulo of a vector (point to 0,0)
# Pitagoras m = sart(x ** 2 + y ** 2)
def mod(point: Point2D):
    return math.sqrt(point.x ** 2 + point.y ** 2)

# se o angulo for 90 o dot product seria zero 
def dot_prod(pointA: Point2D, pointB: Point2D):
    return pointA.x * pointB.x + pointA.y * pointB.y

# Rotate point counterclockwise by theta (degrees)
def rotate(p: Point, theta: float) -> Point:
    def deg_to_rad(theta):
        '''
        180     -- pi
        theta   -- y
        y = pi.theta / 180
        '''
        return theta * math.pi / 180.0

    rad = deg_to_rad(theta)
    return Point(p.x * math.cos(rad) - p.y * math.sin(rad), p.x * math.sin(rad) + p.y * math.cos(rad))

# Só consigo comparar points porque dei override do metodo __lt__
l_p = [Point2D(2,3),Point2D(-1,3),Point2D(2,4),Point2D(3,99)]
print(mod(Point2D(3, 4)))
print(dot_prod(Point2D(2, 4), Point2D(3, 7)))
print(sorted(l_p))