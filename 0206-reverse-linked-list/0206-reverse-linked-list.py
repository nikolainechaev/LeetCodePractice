
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            nextL = curr.next
            
            curr.next = prev
            prev = curr
            curr = nextL
            
        return prev
            