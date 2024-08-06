class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None 
        
        while cur:
            nextNode = cur.next
            
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev