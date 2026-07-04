class Queue:
    def __init__(self):
        self.elements = []
        self.start = -1
        self.end = -1
        self.current_size = 0
        self.maximum_size = 10
    
    def push(self, e):
        if self.current_size + 1 < self.maximum_size:
            self.current_size += 1
            self.elements.append(e)
            end += 1