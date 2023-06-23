class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        
        for r in range(len(nums)):
            for l in range(0,r):
                dp[(r, nums[r] - nums[l])] = dp.get((l, nums[r] - nums[l]), 1) + 1   
        
        return max(dp.values())
        