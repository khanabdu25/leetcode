from deque import Deque

class MovingAverage:
    def __init__(self, size):
        self.queue = Deque()
        self.size = size
        self.total = 0

    def next(self, val):
        
        self.queue.add_rear(val)
        self.total += val
        
        deq_len = self.queue.size()
        
        if deq_len > self.size:
            rm = self.queue.remove_front()
            self.total -= rm
        
        
            
        return self.total / (self.queue.size())
        
        
    