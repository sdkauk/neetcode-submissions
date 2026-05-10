# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        #Step 1, find the correct node
        #Step 2 Check if its a leaf node and and easy case
        #Step 3, if its the hard case, find the smallest node on the right subtree
        #Step 4, replace the value of the node you are removing with the value of the smallest node
        #Step 5, remove that smallest node

        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                root = root.right
                return root
            elif not root.right:
                root = root.left
                return root
            
            minValueNode = self.findMinValueNode(root.right)
            root.val = minValueNode.val
            root.right = self.deleteNode(root.right, root.val)

        return root

    def findMinValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left

        return curr

            