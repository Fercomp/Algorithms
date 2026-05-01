# leetcode.com/problems/group-anagrams/
from collections import defaultdict

def groupAnagrams(strs):
    def createKey(string):
        frequencies = [0] * 26
        for char in string:
            index = ord('a') - ord(char)
            frequencies[index] += 1
        key = "-".join(map(str, frequencies))
        return key
    
    dic = defaultdict(list)
    for s in strs:
        key = createKey(s)
        dic[key].append(s)
    
    result = []
    for value in dic.values():
        result.append(value)
    return result