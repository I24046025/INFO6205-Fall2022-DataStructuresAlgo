# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        
        # get the length and the tail
        length = 1
        tail = head
        
        while(tail.next != None):
            length +=1
            tail = tail.next
        
        # deal with situation that k > length
        k = k%length
        if k == 0:
            return head
        
        # rotate the list
        current = head
        for i in range(length-k-1):
            current = current.next
        
        newHead = current.next
        current.next = None
        tail.next = head;
        return newHead
