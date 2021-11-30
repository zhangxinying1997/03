class Node(object):
    def __init__(self, value, next_=None):
        self._value = value
        self._next = next_


class linked_list(object):
    def __init__(self, node):
        assert isinstance(node._value, int) or isinstance(node._value, Node)
        assert isinstance(node._next, Node) or (node._next == None)
        self.node = node

    @property
    def value(self):
        return self.node._value

    @property
    def next_(self):
        return self.node._next


    def __iter__(self):
        current = self.node
        if isinstance(current._next, Node):
            yield current._value
            yield from linked_list(current._next)
        else:
            yield current._value


def flatten_linked_list( node):
    link_list= []
    for i in linked_list(node):
        if not isinstance(i, Node):
            link_list.append(i)
        else:
            a= flatten_linked_list(i)
            link_list =link_list+a
    return link_list

if __name__ == '__main__':
    r2 = Node(7, Node(2, Node(9)))
    print(flatten_linked_list(r2))
    r3 = Node(3, Node(Node(19, Node(25)), Node(12)))
    r3_flattenned = flatten_linked_list(r3)
    r3_expected_flattenned_collection = [3, 19, 25, 12]
    assert r3_expected_flattenned_collection == list(r3_flattenned)