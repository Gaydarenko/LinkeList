import unittest
import linkedlist
import node


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = linkedlist.LinkedList()

    def test_insert(self):
        self.linked_list.insert(2, 4)
        self.assertEqual(1, len(self.linked_list))
        self.assertEqual(4, self.linked_list._LinkedList__head.value)
        self.assertEqual(4, self.linked_list._LinkedList__tail.value)
        self.linked_list.clear()

        self.linked_list.insert(5, 10)
        self.assertEqual(1, len(self.linked_list))
        self.assertEqual(10, self.linked_list._LinkedList__head.value)
        self.assertEqual(10, self.linked_list._LinkedList__tail.value)
        self.linked_list.insert(0, 11)
        self.assertEqual(2, len(self.linked_list))
        self.assertEqual(11, self.linked_list._LinkedList__head.value)
        self.assertEqual(10, self.linked_list._LinkedList__tail.value)
        self.linked_list.insert(2, 9)
        self.assertEqual(len(self.linked_list), 3)
        self.assertEqual(self.linked_list._LinkedList__head.value, 11)
        self.assertEqual(self.linked_list._LinkedList__tail.value, 9)

        self.assertRaises(IndexError, self.linked_list.insert, -2, 77)

    def test_clear(self):
        self.assertEqual(0, len(self.linked_list))

    def test_append_to_list(self):
        self.linked_list.append(6)
        self.assertEqual(1, len(self.linked_list))
        self.assertEqual(6, self.linked_list._LinkedList__head.value)
        self.assertEqual(6, self.linked_list._LinkedList__tail.value)
        self.linked_list.append(55)
        self.assertEqual(len(self.linked_list), 2)
        self.assertEqual(6, self.linked_list._LinkedList__head.value)
        self.assertEqual(55, self.linked_list._LinkedList__tail.value)

    def test_find(self):
        self.assertEqual(0, len(self.linked_list))
        for i in range(8):
            self.linked_list.append(f"num - {i}")
        self.linked_list.append("num - 0")
        self.assertEqual(0, self.linked_list.find("num - 0"))
        self.assertEqual(7, self.linked_list.find("num - 7"))
        self.assertEqual(-1, self.linked_list.find("num - 8"))

    def test_remove(self):
        for i in range(8):
            self.linked_list.append(f"num - {i}")
        self.linked_list.append("num - 0")
        self.assertEqual(0, self.linked_list.find("num - 0"))
        self.linked_list.remove("num - 0")
        self.assertEqual(7, self.linked_list.find("num - 0"))

    def test_delete(self):
        for i in range(8):
            self.linked_list.append(f"num - {i}")
        self.linked_list.append("num - 0")
        self.linked_list.delete(0)
        self.assertEqual(7, self.linked_list.find("num - 0"))


if __name__ == "__main__":
    unittest.main()