h = [2,3,10,5,7,8,9]

def calculate_area(ha, ia, hb, ib):
    height = min(ha, hb)
    i_min = min(ia, ib)
    i_max = max(ia, ib)
    width = i_max - i_min
    return height * width

def maxArea(height):
    left = 0
    right = 1
    max_area = calculate_area(height[left], left, height[right], right)
    for i in range(2, len(height)):
        a = calculate_area(height[left], left, height[i], i)
        b = calculate_area(height[right], right, height[i], i)
        if a > b and a > max_area:
            right = i
            max_area = a
        elif b > a and b > max_area:
            left = right
            right = i
            max_area = b
    return max_area
        
print(maxArea(h))