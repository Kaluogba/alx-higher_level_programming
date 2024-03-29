#!/usr/bin/python3
"""Classes Node and SinglyLinkedList that define a singly linked list."""


class Node:
    """A class to define a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the Node instance.

        Args:
            data (int): The data value for the node.
            next_node (Node): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the value of the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of the data attribute.

        Args:
            value (int): The data value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the value of the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the value of the next_node attribute.

        Args:
            value (Node): The next node value to set.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class to define a singly linked list."""

    def __init__(self):
        """Initialize the SinglyLinkedList instance."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                    current.next_node.data < value):

                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()


if __name__ == "__main__":
    llist = SinglyLinkedList()
    llist.sorted_insert(5)
    llist.sorted_insert(10)
    llist.sorted_insert(7)
    print(llist)
