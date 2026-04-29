class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        #We start by initializing a dummy node here.
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        #this is how we iterate through the list:
        cur = self.head.next
        i = 0
        while cur:
            if (i >= index):
                return cur.val
            i += 1
            cur = cur.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while i < index and cur:
            i += 1
            cur = cur.next
            
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        vals = []
        cur = self.head.next
        while cur:
            vals.append(cur.val)
            cur = cur.next
        return vals
        
