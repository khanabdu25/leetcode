from deque import Deque

def first_negative(nums, k):
    start = 0
    end = 1
    
    result = []
    
    queue = Deque()
    
    n_len = len(nums)
    
    
    
    
    if n_len == 1:
        if nums[0] < 0:
            return nums
        else:
            return [0]
    
    last_end = n_len - 1
    last_start = n_len - k
    
   
        
    
    while end <= last_end and start <= last_start:
        first_neg = None
        if nums[start] < 0:
            first_neg = nums[start]
        while (end - start) < k:
            if first_neg is None:
                if nums[end] < 0:
                    first_neg = nums[end]
                    # print(f"first_neg updated to {first_neg} due to index {end}")
            end += 1
        end -= 1
        to_append = 0
        if first_neg is not None:
            to_append = first_neg
        # print(f"reaching the appending with end index: {end}")
        result.append(to_append)
        start += 1
        
            
        
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