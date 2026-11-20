def longest_common_prefix(strs):
    strs_len = len(strs)
    if strs_len == 0:
        return ""
    elif strs_len == 1:
        return strs[0]
    
    first_string = strs[0]
    pref = ""
    
    fs_len = len(first_string)
    
    for i in range(fs_len):
        char = first_string[i]
        for index, member in enumerate(strs):
            member_len = len(member)
            if index == 0:
                continue
            elif i > member_len - 1:
                return pref
            elif member[i] != char:
                return pref
        
        pref += char
            
            
    return pref

print(longest_common_prefix(["fff", "fffp", "f"]))  # "f"
print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))  # ""
print(longest_common_prefix(["interview", "internet", "internal"]))  # "inter"
print(longest_common_prefix(["apple", "apple", "apple"]))  # "apple"
print(longest_common_prefix(["a"]))  # "a"
print(longest_common_prefix([]))  # ""
print(longest_common_prefix(["", "abc"]))  # ""
print(longest_common_prefix(["abc", ""]))  # ""
print(longest_common_prefix(["abc", "abcd", "ab"]))  # "ab"
print(longest_common_prefix(["prefix", "preach", "prevent"]))  # "pre"
print(longest_common_prefix(["ppp", "ppp", "pppf"]))  # "ppp"
print(longest_common_prefix(["ppp", "p", "pppf"]))  # "p"
print(longest_common_prefix(["ppp", "ppp", "zppf"]))  # ""