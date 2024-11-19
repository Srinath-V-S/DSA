
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)


def pre_order_traversal_iterative(node):
    stack = [node]

    while stack:
        node = stack.pop()
        # process right first since we are using stacks.
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        print(node)


def main():
    #        1
    #     2    3
    #   4  5  10

    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(10)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F


    pre_order_traversal_iterative(A)


if __name__== '__main__':
    main()
    