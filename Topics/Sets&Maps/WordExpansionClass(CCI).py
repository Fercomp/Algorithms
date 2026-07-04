class Chekcer:
    def __init__(self, s):
        self.s = s
        self.v = self.create_freq_vector(s)
    
    def create_freq_vector(self, s):
        v = [0] * 26
        for i in s:
            index = ord("a") - ord(i)
            v[index] += 1
        return v

    # Time: O(n)
    # Space: O(n)
    def expand_into(self, s2):
        v2 = self.create_freq_vector(s2)
        one_value_diff= False
        
        for i in range(len(v2)):
            if v2[i] == self.v[i]:
                continue
            
            elif v2[i] < self.v[i]:
                return False
            
            else:
                if v2[i] - self.v[i] == 1 and not one_value_diff:
                    one_value_diff = True
                else:
                    return False
              
        return one_value_diff
    
# Tests
checker = Chekcer("tea")
print(checker.expand_into("tea"))
print(checker.expand_into("team"))
print(checker.expand_into("seam"))

checker = Chekcer("on")
print(checker.expand_into("nooo"))
print(checker.expand_into("not"))
print(checker.expand_into("now"))