from stack import Stack

def next_greater_element(nums):
    n_len = len(nums)
    if not nums or n_len == 0:
        return []
    
    result = [-1] * n_len
    
    if n_len == 1:
        return result
    
    stack = Stack()
    
    for index, num in enumerate(nums):
        if not stack.is_empty():
            while not stack.is_empty():
                top_index = stack.peek()
                if num > nums[top_index]:
                    popped = stack.pop()
                    result[popped] = num
                else:
                    break
        
        stack.push(index)
                
                
        
    return result

print(next_greater_element([4, 5, 2, 10]))       # [5, 10, 10, -1]
print(next_greater_element([3, 2, 1]))            # [-1, -1, -1]
print(next_greater_element([1, 2, 3]))             # [2, 3, -1]
print(next_greater_element([2, 2, 2]))             # [-1, -1, -1]
print(next_greater_element([1, 3, 2, 4]))          # [3, 4, 4, -1]
print(next_greater_element([]))                   # []
print(next_greater_element([7]))                  # [-1]
print(next_greater_element([5, 1, 6, 2, 7]))       # [6, 6, 7, 7, -1]
print(next_greater_element([9, 8, 7, 6, 10]))      # [10, 10, 10, 10, -1]
print(next_greater_element([-2, -1, -3, 0]))      # [-1, 0, 0, -1]
print(next_greater_element([1, 1, 2, 2, 3]))       # [2, 2, 3, 3, -1]