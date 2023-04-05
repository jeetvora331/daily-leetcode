class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = nums[0]
        cache = nums[0]
        
        for i in range(1, len(nums)):
            cache += nums[i]
            temp = math.ceil(cache/(i+1))
            res = max(res, temp)
        return res