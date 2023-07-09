# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left = dummy
        right = head 
        
        for _ in range(n):
            right = right.next
            
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return dummy.next
        
        
        # Sliding Window NeetCode
#         extra = ListNode(0 ,head)
#         left = extra
#         right = head

#         while n >0 :
#             right = right.next
#             n = n -1 
            
#         while right:
#             left = left.next
#             right = right.next
        
#         left.next = left.next.next

#         return extra.next



#         My method 
#         last = head 
#         count = 0
#         while last:
#             last = last.next
#             count +=1
        
#         count = count -n 
        


#         if count == 0:
#             return head.next 

#         curr = head
#         for _ in range(count - 1):
#             curr = curr.next

#         curr.next = curr.next.next
#         return head

