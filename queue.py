from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]
        
    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.popleft()
        
    def get(self, index):
        if self.is_empty():
            return None
        else:
            return self.queue[index]
        
    def size(self):
        return len(self.queue)
        
    def is_empty(self):
        return self.size() == 0
    
    def printd(self):
        print(self.queue)