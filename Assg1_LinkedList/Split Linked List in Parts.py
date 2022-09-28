# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
    
        # get the length of lineked list
        tail = head
        length = 0
        
        while tail:
            length += 1
            tail = tail.next
        
        arr = [None for i in range(k)]
        
        mod = length % k
        number = length // k
        
        # create a prev node points to head
        prev = ListNode(0, head)
        curr = head
        
        # the first "mod" groups have number+1 elements
        for i in range(k):
            arr[i] = head
            for j in range(number + (1 if mod > 0 else 0)):
                prev = curr
                curr = curr.next
            mod -= 1
                
            if prev: 
                prev.next = None
            head = curr
            
        return arr