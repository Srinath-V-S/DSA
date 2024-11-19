class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def searchBinaryTree(node,target):
    if not node:
        return False

    if node.val == target:
        return True


    return searchBinaryTree(node.left,target) or searchBinaryTree(node.right,target)


def searchBST(node, target):
    if not node:
        return False

    if node.val == target:
        return True

    if target < node.val:
        return searchBST(node.left,target)
    else:
        return searchBST(node.right,target)


def main():
    #        5
    #     2     8
    #    1  3  4  10

    A = TreeNode(5)
    B = TreeNode(2)
    C = TreeNode(8)
    E = TreeNode(1)
    F = TreeNode(3)
    G = TreeNode(4)
    H = TreeNode(10)
    A.left = B
    A.right = C
    C.left,C.right = G,H
    B.left,B.right = E,F

    isTargetFound = searchBinaryTree(A,10)
    if isTargetFound:
        print("target found")
    else:
        print("target not found")

    isTargetFound = searchBST(A, 59)
    if isTargetFound:
        print("target found")
    else:
        print("target not found")


if __name__=='__main__':
    main()

