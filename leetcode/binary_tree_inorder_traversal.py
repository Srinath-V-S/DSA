# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        result = []

        def traversal(node):
            if not node:
                return

            traversal(node.left)
            result.append(node.val)
            traversal(node.right)

        traversal(root)
        return result