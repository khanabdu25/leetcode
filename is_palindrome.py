def is_palindrome(s):
    the_length = len(s)
    if the_length <= 1:
        return True
    
    # is_even = the_length % 2 == 0
    
    the_middle = the_length //2
    # if is_even is True:
    #     the_middle = int(the_length /2)
    # else:
    #     the_middle = the_length //2
    
    zero_indexed_length = the_length - 1
    for i in range(the_middle):
       if not s[i] == s[zero_indexed_length - i]:
        return False
    
    return True
        
    
   

print(is_palindrome("racecar"))
print(is_palindrome("madam"))
print(is_palindrome("hello"))
print(is_palindrome("a"))
print(is_palindrome(""))
print(is_palindrome("abba"))
print(is_palindrome("zoom"))
print(is_palindrome("stanleyyelnats"))