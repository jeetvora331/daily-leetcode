# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def travel(node):
            if node:
                return travel(node.left) + travel(node.right) +1
            return 0
        
        return travel(root)
        