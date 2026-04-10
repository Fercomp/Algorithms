# leetcode.com/problems/number-of-1-bits/

def hammingWeight(n):
    # Python function to know the number of bits in a binary representation a number n
    l = n.bit_length()
    count = 0
    for i in range(l):
        # mask is a bit string with only the ith term equals to 1 and the rest zero
        mask = 1 << i
        # and operation so i know if the ith bit of the nember n is equal to one
        # the condition is true only if this element equals 1
        if mask & n:
            count += 1
            
    return count