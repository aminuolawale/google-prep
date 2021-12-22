from typing import List, Any

class DoublyLinkedListNode:
    __slots__ = "val", "next"
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



    def append(self, value:int) -> None:
        """"""
        
