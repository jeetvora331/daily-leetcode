class Solution:
    def mostPoints(self, ques: List[List[int]]) -> int:
        dp = {}
        
        def dfs(i):
            
            if i >= len(ques):
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] =  max(dfs(i+1) ,
            ques[i][0] + dfs(i+1+ques[i][1]))
            
            return dp[i]
        
        return dfs(0)