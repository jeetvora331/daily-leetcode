# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for i in range(k-1):
            curr = curr.next
        
        temp = curr
        second = head 
        
        while curr.next:
            curr = curr.next
            second = second.next
            
        temp.val, second.val = second.val, temp.val
        
        return head 
        

        