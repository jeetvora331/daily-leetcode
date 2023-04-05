class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        total = nums[0]
        
        for i in range(1, len(nums)):
            total += nums[i]
            temp = math.ceil(total/(i+1))
            res = max(res, temp)
        return res