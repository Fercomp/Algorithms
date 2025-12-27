# hackerrank.com/challenges/find-second-maximum-number-in-a-list
import math

arr = [2, 5, 1, 9, 8, 7, 9, 3]

# Time: O(nlogn) to sort
# Space: O(1)
def solution1(arr):
    arr = sorted(arr)
    runner_up = -1
    first = arr[-1]
    for i in range(len(arr) -2, -1, -1):
        if arr[i] != first:
            runner_up = arr[i]
            break
    print(runner_up)

# Time: O(n)
# Space: O(1)
def solution2(arr):
    first = -math.inf
    second = -math.inf
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    print(second)

# Time: O(n) to create set
# Space: O(n) of set  
def solution3(arr):
    arr = set(arr)
    arr.remove(max(arr))
    print(max(arr))