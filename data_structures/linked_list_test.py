import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_initialize_linked_list(self):
        linked_list = LinkedList()
        self.assertEqual(linked_list, [])

    def test_append_linked_list(self):
        array = [1,2,3,5,4]
        linked_list = LinkedList()
        for num in array:
            linked_list.append(num)
        self.assertEqual(linked_list, array)
        self.assertEqual(linked_list.size, len(array))

    def test_insert_linked_list(self):
        array = [1,2,3,5,4]
        linked_list = LinkedList()
        for num in array:
            linked_list.append(num)
        linked_list.insert(3, 11)
        self.assertEqual([1, 2, 3, 11, 5, 4], linked_list)
        self.assertEqual(len(array)+1, linked_list.size)

    def test_insert_linked_list(self):
        array = [1, 2, 3, 4, 5]
        linked_list = LinkedList()
        for num in array:
            linked_list.append(num)
        array1 = [6, 7, 8]
        linked_list.extend(array1)
        self.assertEqual(linked_list, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(linked_list.size, 8)

    def test_remove_linked_list(self):
        array = [1,2,3,5,4]
        linked_list = LinkedList()
        for num in array:
            linked_list.append(num)
        linked_list.remove(1)
        self.assertEqual([1, 3, 5, 4], linked_list)
        self.assertEqual(len(array)-1, linked_list.size)
        



if __name__ == "__main__":
    unittest.main()