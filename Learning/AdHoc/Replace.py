_ = input()
s = input()

matches = ["axa", "ixi", "uxu", "exe", "oxo"]
for m in matches:
    s = s.replace(m, "...")
    
print(s)