# Time: O(n + R) where R = smallest - gratest
# Space: O(n)
def counting_sort(nums):
    smallest, gratest = min(nums), max(nums)
    frequency = [0] * (gratest - smallest + 1)
    
    for num in nums:
        frequency[num - smallest] += 1
    
    result = []
    for i in range(len(frequency)):
        if frequency[i] != 0:
            for _ in range(frequency[i]):
                result.append(i + smallest)
    
    return result

print(counting_sort([105, 102, 101, 103, 102, 102, 105]))