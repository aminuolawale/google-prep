from typing import List, Optional, Any

class DynamicArray:
    __slots__ = "capacity", "current_index", "_content"

    def __init__(self, initial: Optional[List[Any]] = None) -> None:
        self.capacity = len(initial) if initial is not None else 1
        self.current_index = len(initial) if initial is not None else 0
        self._content = initial or  [None]

    def append(self, value:Any) -> None:
        if self.current_index < self.capacity:
            self._content[self.current_index] = value
        else:
            self._grow_array()
            self._content[self.current_index] = value
        self.current_index += 1
        

    def __str__(self) -> str:
        return str([a for a in self._content[:self.current_index]])

    def __getitem__(self, index:int) -> Any:
        if index >= self.current_index:
            raise IndexError("Array index is out of range")
        return self._content[index]
    
    def __setitem__(self, index:int, value:Any) -> None:
        if index >= self.current_index:
            raise IndexError("Array index is out of range")
        self._content[index] = value

    def __len__(self) -> int:
        return self.current_index

    def __eq__(self, array:List[Any]) -> bool:
        return str(array) == str(self)
    
    def _grow_array(self):
        self.capacity *= 2
        old_content = self._content
        self._content = [None for _ in range(self.capacity)]
        for i, val in enumerate(old_content):
            self._content[i] = val

    
    def insert(self, index:int, value:Any) -> None:
        if index >= self.current_index:
            raise IndexError("Array index is out of range")
        if self.current_index == self.capacity:
            self._grow_array()
        position = self.current_index
        while position > index:
            self._content[position] = self._content[position -1]
            position -= 1
        self._content[index] = value
        self.current_index += 1

    def remove(self, index:int) -> Any:
        position = index
        while position < self.current_index - 1:
            self._content[position] = self._content[position+1]
            position += 1
        self._content[position] = None
        self.current_index -= 1

    def index(self, value:Any) -> int:
        for i, val in enumerate(self._content[:self.current_index]):
            if val == value:
                return i
        return -1

    def contains(self, value:Any) -> bool:
        return self.index(value) > -1

if __name__ == "__main__":
    array = DynamicArray([122, 5, 7, 11])
    print(array == [122, 5, 7, 11])