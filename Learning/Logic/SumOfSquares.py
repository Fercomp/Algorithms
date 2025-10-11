# Naive approach using list comprehension
def sum_of_squares1(n):
    return sum([i ** 2 for i in range(1, n+1)])
    
# Using square sum formula n(n+1)(2n+1)/6
def sum_of_squares2(n):
    return int(n * (n + 1) * ((2 * n) + 1) * (1/6))

print(sum_of_squares1(10))
print(sum_of_squares2(10))
print(sum_of_squares1(20))
print(sum_of_squares2(20))
