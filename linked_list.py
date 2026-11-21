from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            new = Node(value)
            self.tail.next = new
            self.tail = new

        self.len += 1

    def prepend(self, value):
        if self.head is None:
            self.append(value)
        else:
            new = Node(value)
            new.next = self.head
            self.head = new
            self.len += 1

    def display(self):
        jumper = self.head
        display_list = []
        if jumper is None:
            return display_list
        display_list.append(jumper.value)
        while jumper.next is not None:
            display_list.append(jumper.next.value)
            jumper = jumper.next

        return display_list

    def length(self):
        return self.len

    def search(self, value):
        if self.length() == 0:
            return False

        searcher = self.head
        if searcher.value == value:
            return True
        while searcher.next is not None:
            item = searcher.next.value
            if item == value:
                return True
            searcher = searcher.next

        return False

    def remove(self, value):
        searcher = self.head

        if searcher is None:
            return

        if searcher.value == value:
            # could be removing head or only node
            if searcher.next is None:
                # only node case
                self.head = None
                self.tail = None
            else:
                # remove head case
                self.head = searcher.next
                searcher.next = None

            self.len = self.len - 1
            return

        prev = searcher
        while searcher.next is not None:
            current = searcher.next
            current_val = current.value
            if current_val == value:
                # could be tail or mid node
                prev.next = current.next

                if current.next is None:
                    self.tail = prev

                self.len = self.len - 1
                break

            searcher = searcher.next
            prev = prev.next

    def remove_at(self, index):
        searcher = self.head

        if searcher is None:
            return

        upper = self.length() - 1
        ind = 0

        if index < 0 or index > upper:
            return

        if index == ind:
            # could be removing head or only node
            if searcher.next is None:
                # only node case
                self.head = None
                self.tail = None
            else:
                # remove head case
                self.head = searcher.next
                searcher.next = None

            self.len = self.len - 1
            return

        prev = searcher
        ind += 1
        while searcher.next is not None:
            current = searcher.next

            if index == ind:
                # could be tail or mid node
                prev.next = current.next

                if current.next is None:
                    self.tail = prev

                self.len = self.len - 1
                break

            searcher = searcher.next
            prev = prev.next
            ind += 1

    def insert_at(self, index, value):
        current_len = self.length()
        if index < 0 or index > current_len:
            return

        if index == 0:
            self.prepend(value)
        elif index == current_len or current_len == 0:
            self.append(value)
        else:
            # all else
            prev = self.head
            ind = 1
            while prev.next is not None:
                current = prev.next
                if ind == index:
                    new = Node(value)
                    new.next = current
                    prev.next = new
                    self.len = self.len + 1
                    break

                prev = prev.next
                ind += 1

    def reverse(self):
        if self.head is None:
            return
        if self.head.next is None:
            return
        the_len = self.length()

        previous_2 = None
        previous = self.head
        old_head = self.head
        forward = previous.next
        forward_2 = None
        if the_len != 2:
            forward_2 = forward.next

        while previous is not None:
            forward.next = previous
            previous.next = previous_2
            previous_2 = previous
            previous = forward
            forward = forward_2

            if forward_2 is not None:
                forward_2 = forward_2.next

            else:
                self.head = previous
                self.tail = old_head
                break

    def middle(self):
        if self.head is None:
            return None

        fast = self.head
        slow = self.head

        while slow is not None:
            if fast is None or fast.next is None:
                return slow.value
            slow = slow.next
            fast = fast.next.next

    def has_cycle(self):
        if self.head is None or self.head.next is None:
            return False
        if self.tail.next == self.head:
            return True

        fast = self.head.next.next
        slow = self.head

        while fast is not None:
            if fast == slow:
                return True

            if fast.next is None:
                return False

            if slow is None:
                return False

            fast = fast.next.next
            slow = slow.next

        return False
