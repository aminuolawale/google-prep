from typing import List, Any

class DoublyLinkedListNode:
    __slots__ = "val", "next", "prev"
    def __init__(self, val:int, prev: "DoublyLinkedListNode" = None, next: "DoublyLinkedListNode" = None) -> None:
        self.val = val
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = DoublyLinkedListNode(0)
        self.tail = DoublyLinkedListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _get_contents(self):
        node = self.head.next
        result = []
        while node != self.tail:
            result.append(node.val)
            node = node.next
        return result

    def __getitem__(self, index:int) -> Any:
        if index >= self.size:
            raise IndexError("List index out of range")
        position = -1
        node = self.head
        while position != index:
            node = node.next
            position  +=1
        return node.val


    def __setitem__(self, index:int, value:Any) -> None:
        if index >=self.size:
            raise IndexError("List index out of range")
        position = -1
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
        """ """
        # to append to a doubly-linked list we just need to insert between
        new_node = DoublyLinkedListNode(value)
        old_prev = self.tail.prev
        old_prev.next = new_node
        new_node.prev = old_prev
        new_node.next = self.tail
        self.tail.prev = new_node
        self.size += 1


    def insert(self, index:int, value:Any) -> None:
        if index >= self.size:
            raise IndexError("List index out of range")
        position = -1
        node = self.head
        while position != index:
            node = node.next
            position += 1
        new_node = DoublyLinkedListNode(value)
        prev_node = node.prev
        prev_node.next = new_node
        node.prev = new_node
        new_node.next = node
        new_node.prev = prev_node

    def extend(self, array:List[Any]) -> None:
        for val in array:
            self.append(val)

    def remove(self, index: int) -> Any:
        if index >= self.size:
            raise IndexError("List index out of range")
        node = self.head
        position = -1
        while position != index:
            node = node.next
            position += 1
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        del node