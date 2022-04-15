class Node:
    def __init__(self, value, next_=None, prev_=None):
        self.__next = next_
        self.__prev = prev_
        self.value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        if not isinstance(node, (Node, type(None))):
            raise TypeError
        self.__next = node

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, node):
        if not isinstance(node, (Node, type(None))):
            raise TypeError
        self.__prev = node

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value})"

    def __str__(self):
        return f"{repr(self.__prev)} << {self.value} >> {repr(self.__next)}"
