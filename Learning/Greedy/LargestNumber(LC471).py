from functools import cmp_to_key

def largestNumber(nums):
    n = list(map(str, nums))
    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1
    n.sort(key=cmp_to_key(compare))
    return str(int("".join(n)))

print(largestNumber([3,30,34,5,9]))