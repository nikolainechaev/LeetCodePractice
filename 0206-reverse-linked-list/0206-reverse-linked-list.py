
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            nextValue = curr.next
            
            curr.next = prev
            prev = curr
            curr = nextValue
        return prev