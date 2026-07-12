# leetcode.com/problems/evaluate-reverse-polish-notation

# Time: O(n)
# Space: O(n)
def evalRPN(tokens):
    stack = []
    for t in tokens:
        # Traversing a string takes O(n), while a set lookup takes O(1). However,
        # since this string is only 4 bytes long, it actually takes more time to
        # compute the hash function and use a hash table than to traverse the string.
        # As a rule of thumb, even though a set lookup is O(1), if the collection is
        # very small, it may be better to use a string or an array (list).
        if t in "+-*/":
            r = stack.pop()
            l = stack.pop()
            if t == "+":
                stack.append(l + r)
            elif t == "*":
                stack.append(l * r)
            elif t == "-":
                stack.append(l - r)
            else:
                stack.append(int(l / r))
        
        else:
            stack.append(int(t))

    return stack.pop()