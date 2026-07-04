def robot_instructions(s):
    def helper(s, i):
        if i == len(s):
            return
        
        if s[i] == "2":
            helper(s, i+1)
            helper(s, i+2)
        else:
            print(s[i], end="")
            helper(s, i+1)
            
    helper(list(s), 0)

s = "LL"
robot_instructions(s)
print()
s = "2L"
robot_instructions(s)
print()
s = "22LR"
robot_instructions(s)
print()
s = "LL2R2L"
robot_instructions(s)