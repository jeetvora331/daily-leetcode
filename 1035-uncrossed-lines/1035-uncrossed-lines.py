class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        dp = [ [0]*(n+1) for _ in range(m+1)]
        
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] =  max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]  

#         n1 = len(nums1)
#         n2 = len(nums2)
        
#         memo = {}
        
#         def helper(i, j ):
#             if i<=0 or j<=0:
#                 return 0
            
#             if (i, j) in memo:
#                 return memo[(i, j)]
            
#             if nums1[i-1] == nums2[j-1]:
#                 memo[(i,j)] = 1 + helper(i-1 , j-1)
            
#             else:
#                 memo[(i,j)] = max(helper (i-1 , j), helper (i,j-1))
            
#             return memo[(i,j)]
        
#         return helper(n1,n2)
         