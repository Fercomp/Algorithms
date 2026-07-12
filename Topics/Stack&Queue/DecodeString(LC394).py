from collections import deque

def decodeString(s):
    stack = []

    for char in s:        
        if char == "]":
            partial_s = deque()
            
            while stack[-1] != "[":
                u = stack.pop()
                partial_s.appendleft(u)
            
            
            stack.pop()
            num = deque()
            while stack and "0" <= stack[-1] <= "9":
                x = stack.pop()
                num.appendleft(x)
            
            num = int("".join(num))
            times_s = num * "".join(partial_s)
            stack.append(times_s)
    
        else:
            stack.append(char)
        
    
    return "".join(stack)

print(decodeString("100[leetcode]"))