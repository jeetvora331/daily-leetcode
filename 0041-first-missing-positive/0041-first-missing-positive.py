class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums ==0 or len(nums) == 0: 
            return 1
        
        tab = {}
        
        for n in nums:
            if n > 0:
                tab[n] = True
        
        for k in range(1, len(nums)+1):
            if k not in tab:
                return k
            
        return len(nums)  + 1
        