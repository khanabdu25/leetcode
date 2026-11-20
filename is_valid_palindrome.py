from is_palindrome import is_palindrome

def is_valid_palindrome(s):
    clean = []
    for char in s:
        if char.isalnum():
            clean.append(char.lower())
    clean_string = "".join(clean)
    return is_palindrome(clean_string)

print(is_valid_palindrome("A man, a plan, a canal: Panama"))
print(is_valid_palindrome("race a car"))
print(is_valid_palindrome(" "))
print(is_valid_palindrome("No 'x' in Nixon"))
print(is_valid_palindrome("0P"))
print(is_valid_palindrome("ab_a"))