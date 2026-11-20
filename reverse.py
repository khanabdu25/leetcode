def reverse_string(s):
    the_length = len(s)
    if the_length == 0:
        return s
    reversed_s = ""
    
    n = the_length - 1
    while(n >= 0):
        reversed_s += s[n]
        n = n-1
        
    
    return reversed_s

print(reverse_string("hello"))
print(reverse_string("Python"))
print(reverse_string("a"))
print(reverse_string(""))
print(reverse_string("racecar"))