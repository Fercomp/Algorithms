# cses.fi/problemset/task/1083/

n = int(input())
nums = list(map(int, input().split()))

# Time: O(2n)
# Space: O(n)
def naive_solution():
    s = [0] * n
    for num in nums:
        s[num-1] = 1
    for i in range(len(s)):
        if s[i] == 0:
            print(i + 1)
            
# Time: O(n)
# Space: O(1)
def summation():
    soma = sum(nums)
    print(int(n*(n+1)/2 - soma))

summation()