# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum( root, targetSum):
    """
    :type root: Optional[TreeNode]
    :type targetSum: int
    :rtype: bool
    """

    def traversal(node):
        if not node:
            return False
        print(node.val)

        return (node.val + traversal(node.left) + traversal(node.right)) == targetSum

    return traversal(root)

def main():
    # Create the tree
    #      5
    #     / \
    #    4   8
    #   /   / \
    #  11  13  4
    # /  \      \
    # 7    2      1

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)


    print(hasPathSum(root,22))  # Replace this with your own logic


if __name__ == '__main__':
    main()