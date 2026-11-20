def longest_consecutive(nums):
    unique = set()
    longest = 0
    longests = []
    # dict stores seq_end:seq_start pairs
    tracker = {}
    if not nums:
        return longest

    for num in nums:
        unique.add(num)
    
    for num in unique:
        one_below = num - 1
        if one_below in tracker:
            tracker[num] = tracker[one_below]
            del tracker[one_below]
        else:
            tracker[num] = num
            
    for sequence_end_number, sequence_start_number in tracker.items():
        difference = sequence_end_number - sequence_start_number
        longests.append(difference + 1)
        
            
     
    # print(f"taking max of {longests}")   
    return max(longests)

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 1]))
print(longest_consecutive([3,2,2,1,1]))
print(longest_consecutive([-900, 1, 1, 2, 2, 3]))
print(longest_consecutive([]))
print(longest_consecutive([-200, -500, -499, -498, -497]))
print(longest_consecutive([1,2,3,4,5,99,200, 201, 202]))
print(longest_consecutive([1,2,3,4,5,99,200, 201, 202, 203, 204, 205]))

 # for num in unique:
    #     one_below = num - 1
    #     if one_below in unique:
    #         if one_below in tracker:
    #             tracker[num] = tracker[one_below]
    #             del tracker[one_below]
    #     elif one_below not in unique:
    #         tracker[num] = num