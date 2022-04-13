from node import Node
from typing import Any


class LinkedList:
    """
    This class implements linked list
    """

    def __init__(self):
        """
        Variables initialization
        """
        self.__head = self.__tail = None
        self.len = 0

    def __iter__(self):
        """
        Redetermine iterator
        :return: next node
        """
        current_node = self.__head
        for _ in range(self.len):
            yield current_node
            current_node = current_node.next

    def index_validation(self, index: int) -> None:
        """
        Verification of requirements for index
        :param index: Node position in LinkedList
        :return: None
        """
        if not isinstance(index, int):
            raise IndexError("Index should be integer")
        if index < 0:
            raise IndexError("Index should be positive or zero")

    def insert(self, index: int, value: Any) -> None:
        """
        Insert Node to any place of LinkedList
        :param index: position of node
        :param value: inserting node
        :return: None
        """
        self.index_validation(index)
        insert_node = Node(value)

        if index > self.len:
            self.append(value)

        elif index == 0:
            insert_node.next = self.__head
            self.__head.prev = insert_node
            self.__head = insert_node
            self.len += 1

        else:
            current_node = self.__head
            for _ in range(index - 1):
                current_node = current_node.next
            insert_node.next = current_node.next
            current_node.next = insert_node
            insert_node.prev = current_node
            next_node = insert_node.next
            next_node.prev = insert_node
            self.len += 1

    def append(self, value: Any) -> None:
        """
        Add Node to the tail of LinkedList
        :param value: inserting node
        :return: None
        """
        append_node = Node(value)
        if not self.len:
            self.__head = append_node
            self.__tail = self.__head
        else:
            append_node.prev = self.__tail
            self.__tail.next = append_node
            self.__tail = append_node
        self.len += 1

    def clear(self) -> None:
        """
        Clear LinkedList
        :return: None
        """
        self.__head = None
        self.__tail = None
        self.len = 0

    def find(self, node) -> int:
        ...

    def remove(self, node):
        ...

    def delete(self, index):
        ...


if __name__ == '__main__':
    mylist = LinkedList()
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    mylist.append(4)
    mylist.append(5)
    mylist.insert(0, 10)
    mylist.insert(3, 33)
    print(mylist)
    print(mylist.len)
    a = iter(mylist)
    for _ in range(mylist.len):
        print(next(a))
