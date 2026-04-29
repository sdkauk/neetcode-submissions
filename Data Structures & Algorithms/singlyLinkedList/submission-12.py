class ListNode():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next 
        
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val, self.head.next)
        self.head.next = newNode
        if self.head == self.tail:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val, self.tail.next)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while curr and curr.next:
            if i == index:
                curr.next = curr.next.next
                if curr.next == None:
                    self.tail = curr
                return True
            i+=1
            curr = curr.next
        
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
