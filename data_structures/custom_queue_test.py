import unittest
from custom_queue import CustomQueue


class TestCustomQueue(unittest.TestCase):
    	
	def test_initialize_queue(self):
		""" test Queue """
		q = CustomQueue()
		self.assertIsInstance(q, CustomQueue)
		self.assertTrue(q.isempty())
	
	def test_enqueue(self):
		q = CustomQueue()
		array = [1, 2, 3, 4, 5]
		for val in array:
			q.enqueue(val)
		print(q._contents)
		self.assertEqual(q, array)
	
	def test_dequeue(self):
		q = CustomQueue()
		array = [1, 2, 3, 4, 5]
		for val in array:
			q.enqueue(val)
		a = q.dequeue()
		b = q.dequeue()
		self.assertEqual(q, [3, 4, 5])
		self.assertEqual(a, 1)
		self.assertEqual(b, 2)

	def test_peek_front_queue(self):
		q = CustomQueue()
		array = [1, 2, 3, 4, 5]
		for val in array:
			q.enqueue(val)
		self.assertEqual(q.peek_front(), 1)

	def test_peek_rear_queue(self):
		q = CustomQueue()
		array = [1, 2, 3, 4, 5]
		for val in array:
			q.enqueue(val)
		self.assertEqual(q.peek_rear(), 5)

	

if __name__ == "__main__":
	unittest.main()