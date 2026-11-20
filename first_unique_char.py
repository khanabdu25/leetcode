def first_unique_char(s):
    s_length = len(s)
    if s_length == 0:
        return -1
    
    tracker = {}
    
    for i in range(s_length):
        char = s[i]
        if char in tracker:
            tracker[char].append(i)
        else:
            tracker[char] = [i]
    
    smallest_index = None 
    for char, indices in tracker.items():
        if len(indices) == 1:
            if smallest_index is None:
                smallest_index = indices[0]
            elif indices[0] < smallest_index:
                smallest_index = indices[0]
            
    if smallest_index is None:
        return -1
    else:
        return smallest_index
            
            

print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))
print(first_unique_char("abcabcde"))
print(first_unique_char(""))