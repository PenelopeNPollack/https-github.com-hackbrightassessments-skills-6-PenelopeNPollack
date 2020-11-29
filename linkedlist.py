# Linked list with Node/LinkedList classes


class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node {data}>".format(data=self.data)


class LinkedList(object):
    """Linked List using head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        return "<Linked List head={head}; tail: {tail}>".format(head=self.head, tail=self.tail)

    def add_node(self, data):
        """Add node with data to end of list."""

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node

        apple_node = Node("apple")
        berry_node = Node("berry")
        cherry_node = Node("cherry")

        apple_node.next = berry_node
        berry_node.next = cherry_node


def only_vowels(llist):
    """ Return a new LinkedList object containing nodes with the strings from
    the original linked list that start with vowels. """

    # loop through provided linked list and check to see if first character is a vowel
    # if first character is a vowel, add to new LinkedList

    # return the new linked list

    # llist = LinkedList()
    # llist.add_node("cherry")
    # llist.add_node("berry")
    # llist.add_node("apple")

    # new_llist = only_vowels(llist)
    # new_llist.head.data == "apple"


if __name__ == "__main__":
    import doctest

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
