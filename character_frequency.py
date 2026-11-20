def character_frequency(s):
    freqs = {}
    
    for char in s:
        if not char in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    
    return freqs

print(character_frequency("banana"))
print(character_frequency("hello"))
print(character_frequency("aaa"))
print(character_frequency(""))
print(character_frequency("aabbcc"))