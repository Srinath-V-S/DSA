# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    """
    :type p: Optional[TreeNode]
    :type q: Optional[TreeNode]
    :rtype: bool
    """

    def traversal(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        left = traversal(p.left, q.left)
        if not left:
            return False
        right = traversal(p.right, q.right)
        if not right:
            return False

        return True

    return traversal(p, q)

def main():

    p = TreeNode(1)
    p.left = TreeNode(22)
    p.right = TreeNode(3)

    # Tree 2
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(isSameTree(p, q))  # Replace this with your own logic


if __name__=='__main__':
    main()


