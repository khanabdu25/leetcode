def first_unique_char(s):
    s_length = len(s)
    if s_length == 0:
        return -1
    
    tracker = {}
    
    for char in s:
        tracker[char] = tracker.get(char, 0) + 1
    
   
    for i in range(s_length):
        char = s[i]
        if char in tracker and tracker[char] == 1:
            return i
            
    return -1
            
            

print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))
print(first_unique_char("abcabcde"))
print(first_unique_char(""))