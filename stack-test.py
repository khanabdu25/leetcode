# stack-test.py

from stack import Stack

s1 = Stack()
s2 = Stack()

print(s1.is_empty())  # True
print(s1.pop())       # None
print(s1.peek())      # None

s1.push(10)
s1.push(20)
s1.push(30)

print(s1.peek())      # 30
print(s1.pop())       # 30
print(s1.pop())       # 20
print(s1.peek())      # 10

print(s2.is_empty())  # True (independent stack)
print(s1.is_empty())  # False