import unittest

from data_structures.linkedlist import LinkedList
from data_structures.node import Node

class TestLinkedList(unittest.TestCase):
    def test_list(self):
        linkedlist = LinkedList()

        # insert
        linkedlist.insert_first("First")
        linkedlist.insert_last("Second")
        linkedlist.insert_last("Third")

        linkedlist.insert_first("Befour First")

        self.assertEqual(linkedlist.head.val, "Befour First")
        self.assertEqual(linkedlist.head.next.val, "First")
        self.assertEqual(linkedlist.head.next.next.val, "Second")
        self.assertEqual(linkedlist.head.next.next.next.val, "Third")

        # pop
        linkedlist.pop_first()
        linkedlist.pop_last()

        self.assertEqual(linkedlist.head.val, "First")
        self.assertEqual(linkedlist.head.next.next, None)
        self.assertEqual(linkedlist.pop_first(), "First")
        self.assertEqual(linkedlist.pop_last(), "Second")

        print("Linked list is working fine")


if __name__ == '__main__':
    unittest.main()