# leetcode.com/problems/two-sum

def twoSum(nums, target):
    # A map to store {number: index}
    num_to_index_map = {}

    # Use enumerate to get both the index (i) and the value (num)
    # This strategy of in one pass add the values to dict avoid the problem
    # of first creating a dict and them pass looking for values, because this 
    # could lead to problem of using the same number two times
    # with only one pass we always compare the current number only against previus numbers
    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement we need is already in the map
        if complement in num_to_index_map:
            # If yes, we found the pair. Return the stored index and current index.
            return [num_to_index_map[complement], i]
        
        # If no, add the current number and its index to the map
        # for future checks.
        num_to_index_map[num] = i
    return []