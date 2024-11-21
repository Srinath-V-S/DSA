# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    '''
    To reverse a linked list.

    1. We need to change the links(next) in reverse using two pointers prev and curr
    1 - >  2 -> 3 -> None
None Head
prev curr 
    2. As per the output we need to set the tail to none. In our case our tail will be 1 

    curr.next = prev

    but if we do this we will lose the other part of linked list ( 2->3->None)

    3 -> 2 -> 1 -> None

    3. In order to not lose the list we need to have a temp value storing the remaining list

    temp = curr.next (this will hold 2->3->None)

    4. then move the prev node to curr
    5. and curr to the temp

    curr will be none at the end and prev will be the new head of the reversed linked list.

    '''
