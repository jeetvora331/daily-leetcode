# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        valueList = []
        curr = head
        
        while curr:
            valueList.append(curr.val)
            curr = curr.next
            
        return valueList [::] == valueList[::-1]