from typing import Any, List
import unittest
from stack import Stack

class TestStack(unittest.TestCase):
	def test_initialize_stack(self):
		""" test Stack """
		stack = Stack()
		stack.push(1)
		self.assertIsInstance(stack, Stack)
	
	def test_push_stack(self):
		stack = Stack()
		stack.push(1)
		self.assertEqual(stack, [1])

	def test_pop_stack(self):
		stack = Stack()
		array = [1, 2, 3, 4]
		for val in array:
			stack.push(val)
		res = stack.pop()
		self.assertEqual(stack, [1, 2, 3])
		self.assertEqual(res, 4)

	def test_empty_stack(self):
		stack = Stack()
		self.assertTrue(stack.isempty())

if __name__ == "__main__":
	unittest.main()