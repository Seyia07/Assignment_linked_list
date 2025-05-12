class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index == 0:
            self.insert_at_start(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                print("Index out of bounds")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_at_index(self, index):
        if self.head is None:
            print("List is empty")
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                print("Index out of bounds")
                return
            current = current.next
        current.next = current.next.next

    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
