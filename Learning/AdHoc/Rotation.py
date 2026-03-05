n, q = map(int, input().split())
s = str(input())

# Naive
# for _ in range(q):
#     operation, x = map(int, input().split())
#     if operation == 1:
#         aux = s[n-x:]
#         s = aux + s[:n-x]
#     else:
#         print(s[x]) 
        
counter = 0
for _ in range(q):
    operation, x = map(int, input().split())
    if operation == 1:
        counter -= x
    else:
        print(s[(counter + x-1) % n])