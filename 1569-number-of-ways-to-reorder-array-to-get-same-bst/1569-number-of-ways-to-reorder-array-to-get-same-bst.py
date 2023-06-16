class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9 +7
        
        def dfs(nums):
            n = len(nums)
            if n <3:
                return 1
            
            L = [ a for a in nums if a < nums[0]]
            R = [ a for a in nums if a > nums[0]]
            
            return dfs(L) * dfs(R) * comb(n-1 , len(L)%mod)
        
        return (dfs(nums) -1)%mod