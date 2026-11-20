from min_stack import MinStack

# ms = MinStack()
# ms.push(5)
# ms.push(3)
# ms.push(7)
# ms.push(2)


# print(ms.get_min()) # 2
# ms.pop()
# print(ms.get_min()) # 3
# ms.pop()
# print(ms.get_min()) # 3
# ms.pop()
# print(ms.get_min()) # 5

ms2 = MinStack()

ms2.push(8)
ms2.push(4)
ms2.push(6)
ms2.push(4)
ms2.push(2)
ms2.push(9)

print(ms2.get_min())  # 2

ms2.pop()             # Remove 9
print(ms2.get_min())  # 2

ms2.pop()             # Remove 2
print(ms2.get_min())  # 4

ms2.pop()             # Remove 4
print(ms2.get_min())  # 4

ms2.pop()             # Remove 6
print(ms2.get_min())  # 4

ms2.pop()             # Remove 4
print(ms2.get_min())  # 8

ms2.pop()             # Remove 8
print(ms2.get_min())  # None