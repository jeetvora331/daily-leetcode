class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        L = 0
        z = 0
        res = 0
        
        for R in range(n):
            if nums[R] == 0:
                z +=1
            
            while z >1:
                if nums[L] == 0:
                    z -=1
                L +=1
            res = max(res , R - L + 1 -z)
        
        return res -1 if res == n else res 