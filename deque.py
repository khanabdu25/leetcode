from queue import Queue

class Deque(Queue):
    
    def __init__(self):
        super().__init__()
    
    def add_front(self, value):
        self.queue.appendleft(value)
        
    def add_rear(self, value):
        self.enqueue(value)
        
    def remove_front(self):
        return self.dequeue()
    
    def remove_rear(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()
        
    def peek_front(self):
        return self.peek()
    
    def peek_rear(self):
        if self.is_empty():
            return None
        else:
            return self.queue[-1]
        
    
        
    # empty implemented in parent class
    
    