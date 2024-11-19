from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def level_order_traversal(node):
    if not node:
        return
    queue = deque()
    queue.append(node)

    while queue:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        print(node)
# TODO leetcode problem in progress
def level_order_traversal_lc(node):
    if not node:
        return
    queue = deque()
    queue.append(node)
    levelOrderSubList = []
    noLeftNodes = True
    noRightNodes = True
    while queue:
        node = queue.popleft()
        levelOrderSubList.append(node.val)
        if node.left:
            noLeftNodes = False
            queue.append(node.left)
        if node.right:
            noRightNodes = False
            queue.append(node.right)
    print(levelOrderSubList)
    i = 0
    levelOrderList = []
    # Since each level is exponential of order 2^i where i =0,1,2... we can leverage that.
    if noLeftNodes or noRightNodes:
        print([[item] for item in levelOrderSubList])
    else:
        while 0 < len(levelOrderSubList):
            levelOrderList.append(levelOrderSubList[:2**i])
            levelOrderSubList = levelOrderSubList[2**i:]
            i+=1
        print(levelOrderList)

def main():
    #        3
    #     9    20
    #         5  10

    A = TreeNode(3)
    B = TreeNode(9)
    C = TreeNode(20)
    E = TreeNode(15)
    F = TreeNode(7)
    A.left = B
    A.right = C
    C.left = E
    C.right = F

    # level_order_traversal(A)
    level_order_traversal_lc(A)


if __name__ == '__main__':
    main()
