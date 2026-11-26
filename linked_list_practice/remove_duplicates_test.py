from linked_list import LinkedList

# Test 1: Empty linked list
ll = LinkedList()
ll.remove_duplicates()
print(ll.display())  # Expected: []
print(ll.length())  # Expected: 0

print("----------------------")

# Test 2: Single node
ll = LinkedList()
ll.append(10)
ll.remove_duplicates()
print(ll.display())  # Expected: [10]
print(ll.length())  # Expected: 1

print("----------------------")

# Test 3: No duplicates
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.remove_duplicates()
print(ll.display())  # Expected: [1, 2, 3, 4]
print(ll.length())  # Expected: 4

print("----------------------")

# Test 4: All values duplicated
ll = LinkedList()
ll.append(5)
ll.append(5)
ll.append(5)
ll.append(5)
ll.remove_duplicates()
print(ll.display())  # Expected: [5]
print(ll.length())  # Expected: 1

print("----------------------")

# Test 5: Consecutive duplicates
ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(5)
ll.remove_duplicates()
print(ll.display())  # Expected: [1, 2, 3, 4, 5]
print(ll.length())  # Expected: 5

print("----------------------")

# Test 6: Duplicates at the beginning
ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(2)
ll.append(3)
ll.remove_duplicates()
print(ll.display())  # Expected: [1, 2, 3]
print(ll.length())  # Expected: 3

print("----------------------")

# Test 7: Duplicates at the end
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(4)
ll.remove_duplicates()
print(ll.display())  # Expected: [1, 2, 3, 4]
print(ll.length())  # Expected: 4

print("----------------------")

# Test 8: Duplicates across the entire list except the last value
ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(5)
ll.remove_duplicates()
print(ll.display())  # Expected: [1, 2, 3, 4, 5]
print(ll.length())  # Expected: 5
