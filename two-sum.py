def two_sum(nums, target):
    indices = []
    dictionary = {}
    
    for i, num in enumerate(nums):
        difference = target - num
        if difference in dictionary:
            return [i, dictionary[difference]]
        dictionary[num] = i
    
    return indices

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3,3], 6))
print(two_sum([5, -2, 8, 1], 3))