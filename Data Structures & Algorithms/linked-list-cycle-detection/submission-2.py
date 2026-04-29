# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen = set()
        curr = head
        i = 0
        while curr:
            if curr.next and curr.next.val in seen:
                return True
            curr.val = i
            seen.add(i)
            i += 1
            curr = curr.next

        return False


        []