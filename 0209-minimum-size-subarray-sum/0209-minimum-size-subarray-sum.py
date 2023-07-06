class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        R = 0
        curr =0
        
        res = float('inf')
        
        for R in range(len(nums)):
            curr += nums[R]
            
            while curr >= target:
                res = min(res , R-L +1)
                curr -= nums[L]
                L +=1
                
        return res if res!= float('inf') else 0