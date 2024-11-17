class SLL :

    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def reversed_linked_list(node):
    # Use recursion to print the linked list in reverse
    # base case check if it is the end of linked list.
    # 1 -> 2 -> 5 -> 9 -> None
    if node is None:
        return
    reversed_linked_list(node.next)
    print(node)


def main():
    Head = SLL(1)
    A = SLL(2)
    B = SLL(5)
    C = SLL(9)

    Head.next = A
    A.next = B
    B.next = C


    print(Head,A,B,C)

    reversed_linked_list(Head)


if __name__=='__main__':
    main()


'''
function call explanation

Summary of What Happens at Each Step
Phase	Node Passed to Function	Action Taken	Output
Call 1	1	Calls reversed_linked_list(2)	
Call 2	2	Calls reversed_linked_list(5)	
Call 3	5	Calls reversed_linked_list(9)	
Call 4	9	Calls reversed_linked_list(None)	
Call 5 (Base)	None	Returns (base case)	
Unwind 1	9	Prints 9	9
Unwind 2	5	Prints 5	5
Unwind 3	2	Prints 2	2
Unwind 4	1	Prints 1	1

NOTE: When the recursion unwinds, it essentially runs any remaining code that comes after the recursive function call in each instance of the function, and then continues returning up the call stack.

'''