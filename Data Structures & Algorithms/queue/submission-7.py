class ListNode():
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
 
    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newnode = ListNode(value)
        newnode.prev = self.tail.prev
        self.tail.prev.next = newnode
        self.tail.prev = newnode
        newnode.next = self.tail

    def appendleft(self, value: int) -> None:
        newnode = ListNode(value)
        newnode.next = self.head.next
        newnode.prev = self.head
        self.head.next.prev = newnode
        self.head.next = newnode

    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1
        curr = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        curr.prev.next = self.tail
        return curr.val

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        curr = self.head.next
        self.head.next = self.head.next.next
        curr.next.prev = self.head
        return curr.val
