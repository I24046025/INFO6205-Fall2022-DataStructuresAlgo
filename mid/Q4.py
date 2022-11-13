class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
 
 
def sortedInsert(head, addNode):
    # case1
    if head is None or head.val >= addNode.val:
        addNode.next = head
        head = addNode
        return head
 
    # case2
    cur = head
    while cur.next and cur.next.val < addNode.val:
        cur = cur.next
 
    addNode.next = cur.next
    cur.next = addNode
 
    return head
