# https://leetcode.com/problems/happy-number

def square_sum(n):
    if n == 0:
        return 0
    
    r = n % 10
    q = n // 10
    return r * r + square_sum(q)

def isHappy(n: int) -> bool:
    squares_sum = set()
    current_sum = n
    while current_sum not in squares_sum:
        partial_sum = square_sum(current_sum)
        if partial_sum == 1:
            return True
        
        if partial_sum in squares_sum:
            return False
            
        squares_sum.add(partial_sum)
        current_sum = partial_sum
    
print(isHappy(19))