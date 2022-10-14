# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
          return None
        
        count = 0
        p1 = p2 = head
        
        while p1:
          p1 = p1.next
          count += 1
          print(count)
        
        for i in range(int(count/2)-1):
          p2 = p2.next
        
        p2.next = p2.next.next
        
        return head
        