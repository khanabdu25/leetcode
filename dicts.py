def find_duplicates(nums):
    dictionary = {}
    multiple_appears = []
    
    for num in nums:
        if num in dictionary:
            if dictionary[num] == 1:
                multiple_appears.append(num)
            dictionary[num] += 1
        else:
            dictionary[num] = 1
    
    return multiple_appears
    
print(find_duplicates([1, 2, 1, 3,3, 2, 1, 4, 4 , 4 ]))
print(find_duplicates([7,3,3,7]))