def largeGroupPositions(s):
    result = []
    start = 0
    end = 0
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            if end - start + 1 >= 3:
                result.append([start, end])
            start = i
        end = i
            
    if end - start + 1 >= 3:
        result.append([start, end])
        
    return result

print(largeGroupPositions("abcdddeeeeaabbbcddd"))