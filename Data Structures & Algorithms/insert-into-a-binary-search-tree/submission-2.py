# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        curr = root
        prev = None
        while curr:
            if curr.val > val:
                prev = curr
                curr = curr.left
            elif curr.val < val:
                prev = curr
                curr = curr.right

        if prev and prev.val > val:
            prev.left = TreeNode(val)
        elif prev and prev.val < val:
            prev.right = TreeNode(val)
        else:
            return TreeNode(val)

        return root