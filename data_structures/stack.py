from typing import Any, List


class Stack:
    def __init__(self) -> None:
        self.CAPACITY = 1
        self._contents = [None for _ in range(self.CAPACITY)]
        self.index = -1

    def __eq__(self, array: List[Any]) -> bool:
        for val in array[::-1]:
            if self.pop() != val:
                return False
        return self.isempty()

    def push(self, value:Any) -> None:
        self.index += 1
        if self.index == self.CAPACITY:
            self.CAPACITY *= 2 
            new_contents = [None for _ in range(self.CAPACITY)]
            for i, val in enumerate(self._contents):
                new_contents[i] = val
            self._contents = new_contents
        self._contents[self.index] = value
        

    def pop(self):
        res = self._contents[self.index]
        self._contents[self.index] = None
        self.index -= 1
        if self.index < self.CAPACITY//2:
            self.CAPACITY //= 2
            self._contents = self._contents[:self.CAPACITY]
        return res

    def size(self):
        return self.index + 1

    def isempty(self):
        return self.index == -1

    def peek(self):
        return self._contents[self.index]
