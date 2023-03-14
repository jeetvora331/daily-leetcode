# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0:[], 1: [TreeNode()]}
        def helper(n):
            if n in dp:
                return dp[n]
            
            
            
            
            res = []
            
            for left in range(n):
                right = n - left -1 
                leftTree = helper(left)
                rightTree = helper(right) 
                
                # creating Nodes 
                
                for t1 in leftTree:
                    for t2 in rightTree:
                        res.append(TreeNode(0,t1,t2))
            dp[n] = res
                        
            return res
    
        return helper(n)
        
        