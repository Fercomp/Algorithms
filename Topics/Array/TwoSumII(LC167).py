# leetcode.com/problems/two-sum-ii-input-array-is-sorted

# If the sum of the two pointed numbers is greater than the target, 
# we need a smaller sum — so we move the right pointer leftward (to a smaller number).
# If the sum is less than the target,
# we need a larger sum — so we move the left pointer rightward (to a larger number).
# If the sum matches the target, we return the 1-based indices of the two numbers.
def twoSum(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1
    
    # The loop continues while the left pointer is strictly less than the right pointer.
    # We don’t use `<=` because when both pointers meet, there is no valid pair left to check.
    # This is similar to how binary search avoids checking the same middle element twice.
    while left_pointer < right_pointer:
        addition = numbers[left_pointer] + numbers[right_pointer]
        if addition == target:
            return [left_pointer + 1, right_pointer + 1]
        elif addition < target:
            left_pointer += 1
        else:
            right_pointer -= 1

    return [-1, -1]
