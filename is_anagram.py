def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    freqs = {}
    
    for char in s1:
        if not char in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
            
    for char in s2:
        if not char in freqs:
            return False
        else:
            this_char_freq = freqs[char]
            if this_char_freq == 0:
                return False
            else:
                freqs[char] -= 1
                
  
    
    return True

print(is_anagram("listen", "silent"))
print(is_anagram("anagram", "nagaram"))
print(is_anagram("hello", "world"))
print(is_anagram("aabb", "abab"))
print(is_anagram("aabb", "abbb"))
print(is_anagram("", ""))
print(is_anagram("muiz", "muiz"))
print(is_anagram("aabb", "aab"))