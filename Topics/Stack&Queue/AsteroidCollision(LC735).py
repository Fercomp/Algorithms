def asteroidCollision(asteroids):
    def are_equal_sign(x, y):
        return True if x * y > 0 else False

    stack = []

    for asteroid in asteroids:
        if not stack:
            stack.append(asteroid)
            continue
        
        while stack:
            if are_equal_sign(asteroid, stack[-1]):
                stack.append(asteroid)
                break
            
            last = stack[-1]
            if last < 0 and asteroid > 0:
                stack.append(asteroid)
                break

            if abs(last) > abs(asteroid):
                break

            elif abs(last) < abs(asteroid):
                stack.pop()
                if not stack:
                    stack.append(asteroid)
                    break

            else:
                stack.pop()
                break
        
    return stack

asteroidCollision([-2,-2,1,-2])