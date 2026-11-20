def longest_consecutive(nums):
    unique = set()
    longest = 0
    longests = []
    if not nums:
        return longest

    for num in nums:
        unique.add(num)
        
    for num in unique:
        one_below = num - 1
        if one_below not in unique:
            one_above = num + 1
            this_longest = 1
            while one_above in unique:
                this_longest += 1
                one_above +=1
            longests.append(this_longest)
              
    return max(longests)

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 1]))
print(longest_consecutive([3,2,2,1,1]))
print(longest_consecutive([-900, 1, 1, 2, 2, 3]))
print(longest_consecutive([]))
print(longest_consecutive([-200, -500, -499, -498, -497]))
print(longest_consecutive([1,2,3,4,5,99,200, 201, 202]))
print(longest_consecutive([1,2,3,4,5,99,200, 201, 202, 203, 204, 205]))