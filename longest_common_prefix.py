def longest_common_prefix(strs):
    strs_len = len(strs)
    if strs_len == 0:
        return ""
    elif strs_len == 1:
        return strs[0]
    
    first_string = strs[0]
    pref = ""
    
    for i in range(len(first_string)):
        for index, member in enumerate(strs):
            member_len = len(member) - 1
            if index == 0 and i == 0:
                continue
            elif i > member_len:
                continue
            elif len(pref) > member_len:
                return pref
            elif len(pref) > 0 and not member.startswith(pref):
                return pref[:-1]
            elif index == 1:
                pref = pref + member[i]
            
            
            
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