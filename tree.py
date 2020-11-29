"""Tree class and tree node class."""


class Node(object):
    """Node in a tree."""

    def __init__(self, data, children=None):
        children = children or []
        assert isinstance(children, list), \
            "children must be a list!"
        self.data = data
        self.children = children

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Node {data}>".format(data=self.data)

    def find(self, data):
        """Return node object with this data.

        Start here. Return None if not found.
        """

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)


class Tree(object):
    """Tree."""

    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """Reader-friendly representation."""

        return "<Tree root={root}>".format(root=self.root)

    def get_nodes(self, data):
        """ Return a list of nodes with the given data"""

      
        return self.root.find(data)

        


if __name__ == "__main__":
    import doctest

    b1 = Node("B")
    b2 = Node("B")
    e = Node("E")
    c = Node("C", [ b1, e])
    a = Node("A", [b2, c])
    tree = Tree(a)
    tree.get_nodes("L")
    []

    print()
    result = doctest.testmod()
    if not result.failed:
        print("ALL TESTS PASSED. GOOD WORK!")
    print()
