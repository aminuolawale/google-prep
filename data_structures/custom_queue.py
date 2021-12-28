from typing import Any, List


class CustomQueue:
    def __init__(self) -> None:
        self.CAPACITY = 1
        self._contents = [None for _ in range(self.CAPACITY)]
        self.front = 0
        self.rear = -1
        self.size = 0

    def __eq__(self, array: List[Any]) -> bool:
        sublist = self._contents[self.front: self.rear+1]
        print(">>>>", sublist)
        if len(sublist) == len(array):
            return False
        for val1, val2  in zip(array, sublist):
            if val1 != val2:
                return False
        return self.isempty()
        
    def enqueue(self, value: Any) -> None:
        self.rear += 1
        if self.rear == self.CAPACITY:
            self.CAPACITY *= 2
            new_contents = [None for _ in range(self.CAPACITY)]
            for i, val in enumerate(self._contents):
                new_contents[i] = val
            self._contents = new_contents
        self._contents[self.rear] = value
        self.size += 1

    def dequeue(self):
        res = self._contents[self.front] 
        self._contents[self.front] = None
        self.front += 1
        self.size -=1 
        if self.size < self.CAPACITY//2:
            self.CAPACITY //= 2
            new_contents = [None for _ in range(self.CAPACITY)]
            for i, val in enumerate(self._contents[self.front:self.rear+1]):
                new_contents[i] = val
            self._contents = new_contents
            self.front = 0
            self.rear = len(self._contents)-1
        return res

    def peek_front(self):
        return self._contents[self.front]

    def peek_rear(self):
        return self._contents[self.rear]
    
    def isempty(self):
        return self.size == 0