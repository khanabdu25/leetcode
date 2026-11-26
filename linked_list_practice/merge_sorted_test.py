from linked_list import LinkedList


def merge_sorted(list1, list2):
    if not list1:
        return list2

    if not list2:
        return list1

    this = None
    this2 = None
    other = None
    other2 = None

    to_return = None

    if list1.value < list2.value:
        this = list1
        this2 = this.next
        other = list2
        other2 = other.next
        to_return = list1
    else:
        this = list2
        this2 = this.next
        other = list1
        other2 = other.next
        to_return = list2

    while this is not None:
        if this2 is None:
            this.next = other
            break

        if this2.value < other.value:
            this = this.next
            this2 = this2.next
        else:
            if other2 is not None:
                other2 = other2.next
            this.next = other
            this = this.next
            other = other.next
            this.next = this2

    return to_return


# Test 1: Both lists empty
ll1 = LinkedList()
ll2 = LinkedList()
merged = LinkedList()
merged.head = merge_sorted(ll1.head, ll2.head)
print(merged.display())  # Expected: []

print("----------------------")

# Test 2: First list empty
ll1 = LinkedList()
ll2 = LinkedList()
ll2.append(1)
ll2.append(3)
ll2.append(5)
merged = LinkedList()
merged.head = merge_sorted(ll1.head, ll2.head)
print(merged.display())  # Expected: [1, 3, 5]

print("----------------------")

# Test 3: Second list empty
ll1 = LinkedList()
ll1.append(2)
ll1.append(4)
ll1.append(6)
ll2 = LinkedList()
merged = LinkedList()
merged.head = merge_sorted(ll1.head, ll2.head)
print(merged.display())  # Expected: [2, 4, 6]

print("----------------------")

# Test 4: Equal-length lists, alternating values
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)
ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)
merged = LinkedList()
merged.head = merge_sorted(ll1.head, ll2.head)
print(merged.display())  # Expected: [1, 2, 3, 4, 5, 6]

print("----------------------")

# Test 5: Different-length lists
ll1 = LinkedList()
ll1.append(1)
ll1.append(4)
ll1.append(7)
ll2 = LinkedList()
ll2.append(2)
ll2.append(3)
ll2.append(5)
ll2.append(6)
ll2.append(8)
merged = LinkedList()
merged.head = merge_sorted(ll1.head, ll2.head)
print(merged.display())  # Expected: [1, 2, 3, 4, 5, 6, 7, 8]

print("----------------------")

# Test 6: Duplicate values across both lists
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(3)
ll1.append(5)
ll2 = LinkedList()
ll2.append(1)
ll2.append(3)
ll2.append(4)
ll2.append(5)
merged = LinkedList()
merged.head = merge_sorted(ll1.head, ll2.head)
print(merged.display())  # Expected: [1, 1, 3, 3, 3, 4, 5, 5]

print("----------------------")

# Test 7: All values in first list are smaller
ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll2 = LinkedList()
ll2.append(10)
ll2.append(20)
ll2.append(30)
merged = LinkedList()
merged.head = merge_sorted(ll1.head, ll2.head)
print(merged.display())  # Expected: [1, 2, 3, 10, 20, 30]

print("----------------------")

# Test 8: All values in second list are smaller
ll1 = LinkedList()
ll1.append(10)
ll1.append(20)
ll1.append(30)
ll2 = LinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(3)
merged = LinkedList()
merged.head = merge_sorted(ll1.head, ll2.head)
print(merged.display())  # Expected: [1, 2, 3, 10, 20, 30]
