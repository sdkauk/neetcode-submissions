class ListNode():
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def isEmpty(self) -> bool:
        if self.tail == self.head:
            return True
        return False

    def append(self, value: int) -> None:
        newnode = ListNode(value)
        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode

    def appendleft(self, value: int) -> None:
        newnode = ListNode(value)
        newnode.next = self.head.next
        newnode.prev = self.head
        if self.head.next:
            self.head.next.prev = newnode
        else:
            self.tail = newnode
        self.head.next = newnode

    def pop(self) -> int:
        if self.head == self.tail:
            return -1
        val = self.tail.val
        prev = self.tail.prev
        prev.next = prev.next.next
        self.tail = prev
        return val
        
    def popleft(self) -> int:
        if self.head == self.tail:
            return -1
        val = self.head.next.val
        self.head.next = self.head.next.next
        if self.head.next:
            self.head.next.prev = self.head
        else:
            self.head = self.tail
        return val
        