def contains_duplicates(nums):
    nums_set = set()
    for number in nums:
        if number in nums_set:
            return True
        nums_set.add(number)
    return False
    
print(contains_duplicates([1, 2, 3, 1]))
print(contains_duplicates([1, 2, 3, 4]))
print(contains_duplicates([5, 5]))
print(contains_duplicates([7]))
print(contains_duplicates([]))