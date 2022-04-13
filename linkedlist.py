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
        self.__len = 0

    def __iter__(self):
        """
        Redetermine iterator
        :return: next node
        """
        current_node = self.__head
        for _ in range(self.__len):
            yield current_node
            current_node = current_node.next

    def __reversed__(self):
        """
        Redetermine reversed iterator
        :return: previous node
        """
        current_node = self.__tail
        for _ in range(self.__len):
            yield current_node
            current_node = current_node.prev

    def __len__(self) -> int:
        """
        Redetermine command len
        :return: length LinkedList
        """
        return self.__len

    def __repr__(self) -> str:
        """
        Redetermine view
        :return: str
        """
        return ' <-> '.join(str(n) for n in self)

    @staticmethod
    def index_validation(index: int) -> None:
        """
        Validation of requirements for index
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

        if index > self.__len:
            self.append(value)

        elif index == 0:
            insert_node.next = self.__head
            self.__head.prev = insert_node
            self.__head = insert_node
            self.__len += 1

        else:
            current_node = self.__head
            for _ in range(index - 1):
                current_node = current_node.next
            insert_node.next = current_node.next
            current_node.next = insert_node
            insert_node.prev = current_node
            next_node = insert_node.next
            next_node.prev = insert_node
            self.__len += 1

    def append(self, value: Any) -> None:
        """
        Add Node to the tail of LinkedList
        :param value: inserting node
        :return: None
        """
        append_node = Node(value)
        if not self.__len:
            self.__head = append_node
            self.__tail = self.__head
        else:
            append_node.prev = self.__tail
            self.__tail.next = append_node
            self.__tail = append_node
        self.__len += 1

    def clear(self) -> None:
        """
        Clear LinkedList
        :return: None
        """
        self.__head = None
        self.__tail = None
        self.__len = 0

    def find(self, value: Any) -> int:
        """
        Finds the first occurrence of the specified node.
        :param value: node value
        :return: node index or -1 if the value is not found
        """
        for item in enumerate(self):
            if item[1].value == value:
                return item[0]
        else:
            return -1

    def remove(self, value) -> None:
        """
        Remove the first occurrence of the specified node.
        :param value: node value
        :return: None
        """
        if self.__head.value == value:
            self.__head = self.__head.next
            self.__head.prev = None

        else:
            current_node = self.__head
            for _ in range(self.__len - 1):
                if current_node.value == value:
                    prev_node = current_node.prev
                    next_node = current_node.next
                    prev_node.next = next_node
                    next_node.prev = prev_node
                    break
                current_node = current_node.next

            else:
                if self.__tail.value == value:
                    self.__tail = self.__tail.prev
                    self.__tail.next = None
                else:
                    raise ValueError
        self.__len -= 1

    def delete(self, index) -> None:
        """
        Delete node with index
        :param index: node index
        :return: None
        """
        if index - 1 > self.__len:
            raise IndexError
        elif index == 0:
            self.__head = self.__head.next
            self.__head.prev = None
        elif index + 1 == self.__len:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        else:
            current_node = self.__head
            for _ in range(index):
                current_node = current_node.next
            prev_node = current_node.prev
            next_node = current_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        self.__len -= 1


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
    print(len(mylist))
    a = iter(mylist)
    for _ in range(len(mylist)):
        print(next(a))
    print(mylist.find(3))
    print(mylist.find(10))
    print(mylist.find(5))
    print(mylist.find(333))

    print(mylist.find(33))
    print(mylist.find(33))
    mylist.remove(33)
    print(mylist.find(33))

    mylist = LinkedList()
    mylist.append(1)
    mylist.append(2)
    mylist.append(3)
    mylist.append(4)
    mylist.append(5)
    mylist.insert(0, 10)
    mylist.insert(3, 33)
    print(mylist)
    print(len(mylist))
    # mylist.remove(10)
    # mylist.remove(4)
    # mylist.remove(5)
    # mylist.remove(55)
    mylist.delete(0)
    mylist.delete(2)
    mylist.delete(4)
    a = iter(mylist)
    for _ in range(len(mylist)):
        print(next(a))
    print(len(mylist))
