# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # if [] return []
        if head == None:
            return head
        
        # create a dummy node points to head
        dummy = ListNode(next = head)
        
        # create two pointers
        prev = dummy
        curr = head
        
        while curr: 
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return dummy.next