"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if head == None:
            insertNode = Node(insertVal, None)
            insertNode.next = insertNode
            return insertNode
    
        curr = head
        
        # break the loop when finding the insert place
        while curr.next != head:
            if curr.val <= insertVal <= curr.next.val:
                break
            elif curr.val > curr.next.val:
                if curr.val >= insertVal and curr.next.val >= insertVal:
                    break
                if curr.val <= insertVal and curr.next.val <= insertVal:
                    break
            curr= curr.next
            
        # insert the node
        temp = curr.next
        curr.next = Node(insertVal, temp)
        return head