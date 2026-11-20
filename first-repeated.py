def first_repeated(nums):
    unique = set()
    for num in nums:
        if num in unique:
            return num
        unique.add(num)
    return None

print(first_repeated([2, 1, 3, 1, 2]))
print(first_repeated([5,4,5,4]))
print(first_repeated([1,2,3]))
print(first_repeated([7,7]))