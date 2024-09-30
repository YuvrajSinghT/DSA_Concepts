class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev

                return

            current = current.next

    def display(self):
        if self.is_empty():
            print("The doubly linked list is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()

# Example usage
dll = DoublyLinkedList()

dll.append(1)
dll.append(2)
dll.append(3)

dll.display()  # Output: 1 2 3

dll.prepend(0)

dll.display()  # Output: 0 1 2 3

dll.delete(2)

dll.display()  # Output: 0 1 3
