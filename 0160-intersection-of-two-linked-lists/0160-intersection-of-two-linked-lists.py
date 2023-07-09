# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

#         NeetCode Solution
        l1, l2 = headA, headB
        while l1 != l2:
            if l1:
                l1 = l1.next
            else:
                l1 = headB

            if l2:
                l2 = l2.next
            else:
                l2 = headA
        return l1
            
        
        # My Solution 
#         c1 = 0
#         c2 = 0
#         l1 = headA
#         l2 = headB
        
#         while l1:
#             l1 = l1.next
#             c1 +=1
            
#         while l2:
#             l2 = l2.next
#             c2 +=1
        
#         if c2 > c1:
#             while c2 !=c1:
#                 headB = headB.next
#                 c2 -=1
        
#         if c1 > c2:
#             while c2 !=c1:
#                 headA = headA.next
#                 c1 -=1
                
#         while headA:
#             if headA == headB:
#                 return headA
#             headA = headA.next
#             headB = headB.next
            
        