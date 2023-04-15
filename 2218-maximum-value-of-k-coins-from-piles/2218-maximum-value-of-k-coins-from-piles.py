class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0]*(k+1) for i in range(n+1)]
        for i in range(1,n+1):
            for coins in range(0, k+1):
                curr = 0
                for currCoins in range(0 , min(len(piles[i-1]), coins ) +1):
                    if currCoins >0:
                        curr += piles[i-1][currCoins -1]
                    dp[i][coins] = max(dp[i][coins], dp[i-1][coins-currCoins] + curr)
        return dp[n][k]
        