# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Approach 
        
        dummy = ListNode(None)
        dummy.next = head 
        curr = dummy
        
        while curr.next and curr.next.next:
            A = curr.next 
            B = A.next 
            curr.next , A.next, B.next = B , B.next , A 
            curr = A
        
        return dummy.next
            
        
        
        
        
#         # recurssive Solution
#         if not head or not head.next:
#             return head
        
#         A = head
#         B = head.next
#         temp = head.next.next
#         B.next = A
#         A.next = self.swapPairs(temp)
#         return B
        
        