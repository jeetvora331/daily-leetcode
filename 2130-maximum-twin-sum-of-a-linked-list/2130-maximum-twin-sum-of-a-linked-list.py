# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lst = []
        current = head
        while current:
            lst.append(current.val)
            current = current.next
            
        mx = 0
        for i in range(len(lst)):
            curr = lst[i] + lst[-i-1]
            mx = max(mx , curr)
        return mx
        