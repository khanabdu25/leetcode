def find_largest(nums):
    if not nums:
        return None
    
    maximum = nums[0]
    
    for x in nums:
        if (x > maximum):
            maximum = x
    return maximum

print(find_largest([-98, 1, 5, 199, 5600]))
