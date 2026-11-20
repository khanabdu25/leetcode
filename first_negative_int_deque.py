from deque import Deque

def first_negative(nums, k):
    start = 0
    end = k - 1

    queue = Deque()
    
    n_len = len(nums)
    
    windows = n_len - k + 1
    result = [0] * windows
    
    
    last_end = n_len - 1
    last_start = n_len - k
    
    for index, num in enumerate(nums):
        if num < 0:
            queue.add_rear(index)
    
    current_window = 0
    
    # print("------------------------------------------------------")
    # print(f"doing arr: {nums}")
    # queue.printd()
    
    while end <= last_end and start <= last_start:
        # print(f"its the window between {start} and {end}")
        # print(f"result at this index ({current_window}) is {result[current_window]}")
        if result[current_window] == 0:
            pf = queue.peek_front()
            if pf is not None and pf <= end and pf >= start:
                if start + 1 > pf:
                    queue.remove_front()
                # queue.printd()
                num = nums[pf]
                result[current_window] = num
        
        end += 1
        start += 1
        current_window += 1
            
    return result

print(first_negative([12, -1, -7, 8, -15, 30, 16, 28], 3))  # [-1, -1, -7, -15, -15, 0]
print(first_negative([1, 2, 3, 4, 5], 2))                    # [0, 0, 0, 0]
print(first_negative([-1, -2, -3, -4], 2))                  # [-1, -2, -3]
print(first_negative([1, -2, 3, -4, 5], 3))                # [-2, -2, -4]
print(first_negative([-5, 2, 3, 4, 5], 3))                 # [-5, 0, 0]
print(first_negative([1, 2, -3, 4, 5], 5))                 # [-3]
print(first_negative([1, 2, 3, 4, 5], 1))                  # [0, 0, 0, 0, 0]
print(first_negative([-1], 1))                             # [-1]
print(first_negative([1, -1], 1))                          # [0, -1]