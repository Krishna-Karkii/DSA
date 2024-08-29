class Node:
    """This class is the structure of the Node."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """This class represents structure of the linkedlist."""
    def __init__(self):
        self.head = None

    def insert(self, data):
        """This method helps to choose from inserting from beginning
        or end of linkedlist"""

        choice = input("Enter 1 for inserting at beginning or 2 for the end: ")
        if choice.strip() == "1":
            self._insert_at_end(data)
        elif choice.strip() == "2":
            self._insert_at_front(data)
        else:
            print("Please follow the instruction correctly!")

    def _insert_at_end(self, data):
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

    def _insert_at_front(self, data):
        """This inserts an element in the front of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def remove_from_end(self):
        """remove from the end of the linkedlist"""
        if self.head == None:
            print("Linked list is empty")
            return
        last = self.head
        if last.next.next != None:
            last = last.next
        print("Removing Value: ", last.next.data)
        last.next = None

    def traverse(self):
        """traverse the whole linked list."""
        # create temp to traverse to the last node not changing the head
        temp = self.head
        while temp.next != None:
            print(temp.data)
            temp = temp.next
        print(temp.data)


if __name__ == "__main__":
    l_list = LinkedList()
    print("Enter q to quit!")
    prompt = ""

    # loop triggers until the user quits the loop
    while prompt.lower() != "q":
        prompt = input("Enter 1 for inserting, "
                       "2 for deleting, "
                       "3 for traversing: ")
        if prompt == "1":
            data = input("Enter data to insert in the list: ")
            l_list.insert(data.strip())

        elif prompt == "2":
            l_list.remove_from_end()

        elif prompt == "3":
            l_list.traverse()

        else:
            print("Print please follow the command!")

