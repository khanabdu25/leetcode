from stack import Stack

def is_valid(s):
    s_len = len(s)
    
    if s_len == 0:
        return True
    
    if s_len % 2 != 0:
        return False
    
    stak = Stack()
    
    pairs = {
        ")":"(",
        "}": "{",
        "]": "["
    }
    
    for item in s:
        if item in pairs:
            popped = stak.pop()
            if popped != pairs[item]:
                return False
        else:
            stak.push(item)
    
    return stak.is_empty()

print(is_valid("((()"))  # False
print(is_valid("(( "))   # False
print(is_valid("()"))       # True
print(is_valid("()[]{}"))   # True
print(is_valid("(]"))       # False
print(is_valid("([)]"))     # False
print(is_valid("{[]}"))     # True
print(is_valid("((("))      # False
print(is_valid(""))         # True
print(is_valid("]"))        # False
print(is_valid("[(){}]"))   # True
print(is_valid("(([]))"))   # True
print(is_valid("({[]})"))   # True
print(is_valid("(()"))     # False
print(is_valid("())"))     # False
print(is_valid("{[}]"))     # False