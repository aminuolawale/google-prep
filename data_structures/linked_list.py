from typing import List, Any

class LinkedListNode:
    __slots__ = "val", "next"
    def __init__(self, val:int, next: "LinkedListNode" = None) -> None:
        self.val = val
        self.next = next



class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.current_node = self.head
        self.size = 0
    
    def _get_contents(self):
        node = self.head
        result = []
        while node is not None:
            result.append(node.val)
            node = node.next
        return result
        
    def __getitem__(self, index:int) -> Any:
        if index >= self.size:
            raise IndexError("List index out of range")
        position = 0
        node = self.head
        while position != index:
            node = node.next
            position += 1
        return node.val
        
    def __setitem__(self, index:int, value: Any) -> None:
        if index >= self.size:
            raise IndexError("List index out of range")
        position = 0
        node = self.head
        while position != index:
            node = node.next
            position += 1
        node.val = value

    def __eq__(self, array:List[Any]) -> bool:
        return str(array) == str(self)

    
    def __str__(self):
        contents = self._get_contents()
        return str(contents)

    def append(self, value:int) -> None:
        if self.head is None:
            self.head = LinkedListNode(value)
            self.current_node = self.head
        else:
            node = LinkedListNode(value)
            self.current_node.next = node
            self.current_node = node
        self.size += 1

    def insert(self, index:int, value:Any)-> None:
        if index >= self.size:
            raise IndexError("List index out of range")
        position = 0
        prev_node = self.head
        while position != index - 1:
            prev_node = prev_node.next
            position += 1
        new_node = LinkedListNode(value)
        current_node = prev_node.next
        new_node.next = current_node
        prev_node.next = new_node
        self.size += 1

    def remove(self, index: int) -> Any:
        if index >= self.size:
            raise IndexError("List index out of range")
        if index == 0:
            next_node = self.head.next
            del self.head
            self.head = next_node
        else:
            position = 0
            prev_node = self.head
            while position != index - 1:
                prev_node = prev_node.next
                position += 1
            current_node = prev_node.next
            next_node = current_node.next
            prev_node.next = next_node
            del current_node
        self.size -= 1 




if __name__ == "__main__":
    l = LinkedList()
    # l.append(0)
    # l.append(1)
    # l.append(2)
    # l.append(3)
    # l.append(4)
    # l.append(5)
    # l.append(6)
    # l.remove(0)
    # l.remove(0)
    # l.remove(4)
    # l.remove(3)
    print(l)