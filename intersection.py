def intersection(nums1, nums2):
    unique = set()
    in_both = set()
    
    for num in nums2:
        unique.add(num)
            
    for num in nums1:
       if num in unique:
           in_both.add(num)
    
    return list(in_both)

print(intersection([1, 2, 2, 3], [2,2,4]))
print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersection([1, 2], [3,4]))