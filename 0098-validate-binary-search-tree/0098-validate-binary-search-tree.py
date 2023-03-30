# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        arr = []
        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        
        inorder(root)
        for i in range((len(arr) -1)):
            if arr[i] >= arr[i+1]:
                return False
            
        return True
#         def valid(node, L , R):
#             if not node:
#                 return True
            
#             if not( node.val < R and node.val > L ):
#                 return False            
#             return (valid(node.left , L , node.val) and valid(node.right , node.val , R))

#         return valid(root,float("-inf") , float("inf"))