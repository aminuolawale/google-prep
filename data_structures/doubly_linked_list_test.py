import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    	
	def test_initialize_doubly_linked_list(self):
		""" test DoublyLinkedList """
		dlinked_list = DoublyLinkedList()
		self.assertEqual(dlinked_list, [])

	def test_append_doubly_linked_list(self):
		dlinked_list = DoublyLinkedList()
		dlinked_list.append(1)
		self.assertEqual(dlinked_list, [1])

	def test_insert_doubly_linked_list(self):
		dlinked_list = DoublyLinkedList()
		array = [1, 2, 4, 5]
		for val in array:
			dlinked_list.append(val)
		dlinked_list.insert(2, 3)
		self.assertEqual(dlinked_list, [1, 2, 3, 4, 5])
	
	def test_remove_doubly_linked_list(self):
		dlinkedlist = DoublyLinkedList()
		array = [1, 2, 3, 3, 4, 5]
		for val in array:
			dlinkedlist.append(val)
		dlinkedlist.remove(3)
		self.assertEqual(dlinkedlist, [1, 2, 3, 4, 5])

		
if __name__ == "__main__":
	unittest.main()