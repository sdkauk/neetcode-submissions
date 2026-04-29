class ListNode():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newnode = ListNode(val, self.head.next)
        self.head.next = newnode
        if not newnode.next:
            self.tail = newnode
        
    
    def insertTail(self, val: int) -> None:
        newnode = ListNode(val, None)
        self.tail.next = newnode
        self.tail = newnode
    
    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr and i < index:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next.next == None:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


        
