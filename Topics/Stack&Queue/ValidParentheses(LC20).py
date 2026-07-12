# leetcode.com/problems/valid-parentheses

# Time: O(n)
# Space: O(n)
def isValid(s):
    close_to_open = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    stack = []
    for ch in s:
        # if it's not in the dict, it's an opening bracket, so we add it to the stack
        if ch not in close_to_open:
            stack.append(ch)
        else:
            # if there is no opening bracket in the stack and we find a closing bracket, it's invalid
            if not stack:
                return False

            top = stack.pop()
            # if the top of the stack doesn't match the current closing bracket, it's invalid
            if close_to_open[ch] != top:
                return False

    # if we finish processing all characters and still have elements in the stack, it's invalid
    if stack:
        return False

    return True