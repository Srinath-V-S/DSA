# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traversal(node,from_left):
            if not node:
                return 0
            # condition to check if node is a leaf node.
            if not node.left and not node.right and from_left:
                return node.val
            left_sum = traversal(node.left,True)
            right_sum = traversal(node.right,False)
            return left_sum + right_sum


        return traversal(root,False)