from deque import Deque

def get_indexof_max_in_range(start, end, nums):
    most = nums[start]
    indexof_most = start
    for i in range(start, end):
        if nums[i] > most:
            most = nums[i]
            indexof_most = i
            
    return indexof_most
    

def max_sliding_window(nums, k):
    
    if k == 1:
        return nums
    
    start = 0
    end = k - 1
    
    n_len = len(nums)
        
    result = []
        
    last_end = n_len - 1
    last_start = n_len - k
    
    # print("------------------------------------------------------")
    # print(f"doing arr: {nums}")
    
    queue = Deque()
    
    # the next window is made up of only 1 new number
    
    max_index = get_indexof_max_in_range(start, end + 1, nums)
            
    start += 1
    end += 1
    result.append(nums[max_index])
    queue.add_rear(max_index)
    
    while end <= last_end and start <= last_start:
        
        front = queue.peek_front()
        if front is not None and front < start:
            queue.remove_front()
            
        rear = queue.peek_rear()
        if rear is not None:
            if nums[end] >= nums[rear]:
                queue.add_rear(end)
        else:
            max_index = get_indexof_max_in_range(start, end + 1, nums)
            queue.add_rear(max_index)
            
        result.append(nums[queue.peek_rear()])
        # print(f"found max for this range ({start}:{end}) as {nums[queue.peek_rear()]}")    
        start += 1
        end += 1
    
    return result

print(max_sliding_window([10, 1, 9, 8, 7, 6], 3)) # Expected: [10, 9, 9, 8]
print(max_sliding_window([10, 9, 8, 7, 6, 5, 4], 3)) # [10, 9, 8, 7, 6]
print(max_sliding_window([1, 3, -1, -3, 5, 9, 9, 20000, -90, 5, 8, 1, 3, 6, 7], 5))  # [5, 9, 9, 20000, 20000, 20000, 20000, 20000, 8, 8, 8]
print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(max_sliding_window([1], 1))                         # [1]
print(max_sliding_window([1, -1], 1))                     # [1, -1]
print(max_sliding_window([9, 11], 2))                     # [11]
print(max_sliding_window([4, 3, 2, 1], 2))                 # [4, 3, 2]
print(max_sliding_window([1, 2, 3, 4, 5], 3))              # [3, 4, 5]
print(max_sliding_window([5, 5, 5, 5, 5], 3))              # [5, 5, 5]
print(max_sliding_window([-7, -8, -5, -3, -9], 2))         # [-7, -5, -3, -3]
print(max_sliding_window([10, 9, 8, 7, 6, 5], 3))          # [10, 9, 8, 7]
print(max_sliding_window([1, 3, 1, 2, 0, 5], 4))           # [3, 3, 5]