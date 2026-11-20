def is_subset(nums1, nums2):
    unique_nums2 = set()
    for num in nums2:
        unique_nums2.add(num)
        
    for num in nums1:
        if not num in unique_nums2:
            return False
    
    return True
        

print(is_subset([1, 2], [1, 2,3,4]))
print(is_subset([1, 4], [1, 2,3]))
print(is_subset([], [1, 2]))
print(is_subset([2, 2], [1, 2,3]))