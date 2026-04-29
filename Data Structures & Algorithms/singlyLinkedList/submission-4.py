class NewNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = NewNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:

        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new = NewNode(val)
        new.next = self.head.next
        self.head.next = new
        if not new.next:
            self.tail = new

    def insertTail(self, val: int) -> None:
        new = NewNode(val)
        self.tail.next = new
        self.tail = new

    def remove(self, index: int) -> bool:
        
        cur = self.head #the reason we don't want self.head.next is because we want the node PRIOR to the one we need to delete
        i = 0
        while cur:
            if i == index and cur.next:
                if cur.next == self.tail:
                    self.tail = cur
                cur.next = cur.next.next
                return True
            i += 1
            cur = cur.next
        return False

    def getValues(self) -> List[int]:
        newArray = []
        cur = self.head.next
        while cur:
            newArray.append(cur.val)
            cur = cur.next
        return newArray

