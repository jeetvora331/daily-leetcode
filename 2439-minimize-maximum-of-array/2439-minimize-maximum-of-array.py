class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        total = res
        
        for i in range(1, len(nums)):
            total += nums[i]
            res = max(res , math.ceil(total/(i+1)))
        
        return res