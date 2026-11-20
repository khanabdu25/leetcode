from stack import Stack

class MinStack(Stack):
    def __init__(self):
        super().__init__()
        self.mins = []
        
    def get_min(self):
        if self.is_empty():
            return None
        return self.mins[-1]
        
    def push(self, value):
        self.stack.append(value)
        self.update_mins(value)
               
    def pop(self):
        if self.is_empty():
            return None
        pop_return = self.stack.pop()
        self.shuffle_mins(pop_return)
        return pop_return
    
    def shuffle_mins(self, remove):
        if self.mins and remove == self.mins[-1]:
            self.mins.pop()
        
    
    def update_mins(self, value):
        if not self.mins or value <= self.mins[-1]:
            self.mins.append(value)
                