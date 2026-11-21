from linked_list import LinkedList

# Test 1: Empty linked list
ll = LinkedList()
print(ll.nth_from_end(1))  # Expected: None

print("----------------------")

# Test 2: Single-node linked list
ll = LinkedList()
ll.append(10)
print(ll.nth_from_end(1))  # Expected: 10

print("----------------------")

# Test 3: Last node
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
print(ll.nth_from_end(1))  # Expected: 50

print("----------------------")

# Test 4: Second-to-last node
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
print(ll.nth_from_end(2))  # Expected: 40

print("----------------------")

# Test 5: Middle node
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
print(ll.nth_from_end(3))  # Expected: 30

print("----------------------")

# Test 6: First node (n equals list length)
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
print(ll.nth_from_end(5))  # Expected: 10

print("----------------------")

# Test 7: n is zero
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll.nth_from_end(0))  # Expected: None

print("----------------------")

# Test 8: n is negative
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll.nth_from_end(-1))  # Expected: None

print("----------------------")

# Test 9: n exceeds list length
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll.nth_from_end(4))  # Expected: None
