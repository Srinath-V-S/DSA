# Doubly Linked list


class DLL:
    def __init__(self,val,next=None,prev=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.val)

# Single linked list
class SLL:
    # constructor
    def __init__(self,val, next=None):
        self.val = val
        self.next = next


    # Print method
    def __str__(self):
        return str(self.val)



def main():
    # -------------------------------------------------------------------SLL-----------------------------------------------------------------------------------
    # Created singly linked list.
    Head = SLL(1)
    A = SLL(3)
    B = SLL(4)

    Head.next = A
    A.next = B
    B.next = None
    print(Head)
    print(A)
    print(B)


    # Singly Linked List traversal is a O(n)
    # Traversing a SLL
    # Structure  --  Head (1) -> A(3) -> B(4) -> NONE
    current = Head

    while current:
        print(current)
        current = current.next

    print(search(Head,1))
    # =--------------------------------------DLL---------------------------------------------------------------------------------------
    # # Created Doubly linked list.
    # HEAD = TAIL = DLL(1)
    # C = DLL(3)
    # D = DLL(4)
    #
    # HEAD.next = C
    # C.next=D
    # C.prev = HEAD
    # D.next = TAIL
    # D.prev = C
    # TAIL = D
    # print(HEAD.next)
    #
    #
    # # Doubly Linked List traversal is a O(n)
    # # Traversing a DLL
    # # Structure  --  NONE <-> Head (1) <-> C(3) -> D(4) -> NONE
    # currentDLL = HEAD
    # print("########DLL OUTPUT")
    # while currentDLL:
    #     print(currentDLL)
    #     currentDLL = currentDLL.next

# Searching a SLL take O(n)
def search(Head,val):
    current = Head
    while current:
        if val == current.val:
            return True
        current = current.next
    return False




if __name__ == "__main__":
    main()
