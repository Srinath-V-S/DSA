# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        def traversal(node):
            if not node:
                return 0

            left = 1 + traversal(node.left)
            right = 1 + traversal(node.right)
            if left == 1:
                return right
            elif right == 1:
                return left
            else:
                return min(left, right)

        return traversal(root)


