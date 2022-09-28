# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        first = head
        second = head
        
        for i in range(k-1):
            first = first.next
        
        # save the first swapping node as temp
        temp = first
        
        while first.next:
            first = first.next
            second = second.next
        
        # swap data of the two nodes
        temp.val, second.val = second.val, temp.val 
        
        return head