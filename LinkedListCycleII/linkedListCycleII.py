# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def intersection(self,head):
        fast = head
        slow = head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next
            if(slow==fast):
                return slow
        return None
    
    def detectCycle(self, head):
        if head==None or head.next == None:
            return None
        
        theintersect = self.intersection(head)
        if theintersect==None:
            return None
        
        start = head
        while(theintersect!=start):
            start = start.next
            theintersect = theintersect.next
        
        return start
    