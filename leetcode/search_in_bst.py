# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def traversal(node, val):
            if not node:
                return None

            if val == node.val:
                return node

            if val < node.val:
                return traversal(node.left, val)
            else:
                return traversal(node.right, val)

        return traversal(root, val)