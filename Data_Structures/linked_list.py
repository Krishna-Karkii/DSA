class Node:
    """This class is the structure of the Node."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """This class represents structure of the linkedlist."""
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """insert the node at the end of linked_list"""
        new_node = Node(data)

        # head to point at the first node of the linked list
        if self.head == None:
            self.head = new_node
            return

        # traverse to the last node of the linked list
        last = self.head
        while last.next != None:
            last = last.next
        last.next = new_node

    def traverse(self):
        """traverse the whole linked list."""
        # create temp to traverse to the last node not changing the head
        temp = self.head
        while temp.next != None:
            print(temp.data)
            temp = temp.next
        print(temp.data)


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end("Hello")
    ll.insert_at_end("Krishna")
    ll.insert_at_end("Karki")
    ll.traverse()
