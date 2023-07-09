# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        S = head
        F = head
        
        while F and F.next:
            S = S.next
            F = F.next.next
            
            if S==F:
                return True
        return False
        
        
#         S = head
#         F = head
#         while F and F.next:
#             S = S.next
#             F = F.next.next
#             if S == F:
#                 return True
#         return False