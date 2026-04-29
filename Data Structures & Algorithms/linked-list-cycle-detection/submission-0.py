# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = []
        curr = head
        i = 0
        while curr:
            if curr in prev:
                return True
            prev.append(curr)
            curr = curr.next

        return False

