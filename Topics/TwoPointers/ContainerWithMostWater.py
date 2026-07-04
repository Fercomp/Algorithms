import math
h = [1,3,2,5,25,24,5]

def maxArea(height):
    l, r = 0, len(height) -1

    def area(left, right):
        base = right - left
        side = min(height[left], height[right])
        return base * side 

    max_area = -math.inf

    while l <= r:
        max_area = max(max_area, area(l, r))
        
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    
    return max_area
        
print(maxArea(h))