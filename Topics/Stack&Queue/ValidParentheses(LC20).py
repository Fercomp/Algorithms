# leetcode.com/problems/valid-parentheses

# Time: O(n)
# Space: O(n) stack can have up to n elements in the worst case
def isValid(s):
    close_to_open = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    stack = []
    for ch in s:
        # If it's not in the dict, it's an opening bracket,
        # so we always add it to the stack
        if ch not in close_to_open:
            stack.append(ch)
        else:
            # Edge case: if there is no opening bracket in the stack
            # and we find a closing bracket, it's invalid
            if not stack:
                return False

            top = stack.pop()
            # If the top of the stack doesn't match the current closing bracket,
            # it's invalid
            if close_to_open[ch] != top:
                return False

    # Edge case: if we finish processing all characters
    # and still have elements in the stack, it's invalid
    if stack:
        return False

    return True