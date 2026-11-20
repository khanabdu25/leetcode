from deque import Deque

def max_sliding_window(nums, k):
    
    if k == 1:
        return nums
    
    start = 0
    end = k - 1
    
    n_len = len(nums)
        
    windows = n_len - k + 1
    # result = ['*'] * windows
    result = []
        
    last_end = n_len - 1
    last_start = n_len - k
    
    current_window = 0
    
    print("------------------------------------------------------")
    # print(f"doing arr: {nums}")
    
    # the next window is made up of only 1 new number
    
    while end <= last_end and start <= last_start:
        
        max_for_this_window = nums[start]
        for i in range(start, end + 1):
            if nums[i] > max_for_this_window:
                max_for_this_window = nums[i]
        
        result.append(max_for_this_window)
        # print(f"found max for this range ({start}:{end}) as {max_for_this_window}")    
        start += 1
        end += 1
    
    return result

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