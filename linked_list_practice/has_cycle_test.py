from linked_list import LinkedList

# Test 1: Empty linked list
ll = LinkedList()
print(ll.has_cycle())  # Expected: False

print("----------------------")

# Test 2: Normal linked list
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
print(ll.has_cycle())  # Expected: False

print("----------------------")

# Test 3: Cycle back to head
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.tail.next = ll.head
print(ll.has_cycle())  # Expected: True

print("----------------------")

# Test 4: Cycle back to a middle node
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.tail.next = ll.head.next.next  # 50 points back to 30
print(ll.has_cycle())  # Expected: True

print("----------------------")

# Test 5: Self-cycle (one node points to itself)
ll = LinkedList()
ll.append(10)
ll.head.next = ll.head
print(ll.has_cycle())  # Expected: True

print("----------------------")

# Test 6: Cycle involving the last two nodes
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.tail.next = ll.tail  # 40 points to itself
print(ll.has_cycle())  # Expected: True
