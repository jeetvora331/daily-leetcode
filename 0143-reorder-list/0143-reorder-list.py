# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #1 find the middle 
        s = head
        f = head.next

        while f and f.next:
            s = s.next
            f = f.next.next
        
        # 2 invert second half
        second = s.next
        s.next = None 
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second 
            second = temp

        second = prev 
    

        # 3. merge two halves
        first = head 
        second = prev 
        while second : 
            temp1 = first.next 
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

