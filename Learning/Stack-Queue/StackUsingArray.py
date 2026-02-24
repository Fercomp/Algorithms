# Create an stack ds using only array
class Stack:
    def __init__(self):
        self.t = -1
        self.elements = []
        
    def pop(self):
        if self.t > -1:
            aux = self.elements[self.t]
            self.t -= 1
            return aux
        return None
    
    def size(self):
        return self.t + 1
    
    def push(self, e):
        self.t += 1
        self.elements.append(e)
    
    def top(self):
        if self.t > -1:
            return self.elements[self.t]
        return None

s = Stack()  
s.push(4)
s.push(5)
print(s.size())
print(s.top())
print(s.pop())
print(s.size())
print(s.top())