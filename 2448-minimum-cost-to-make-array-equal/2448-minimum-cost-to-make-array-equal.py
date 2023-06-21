class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        def getCost(base):
            return sum(abs(base-num)*c for num , c in zip(nums, cost))
        
        L = min(nums)
        R = max(nums)
        
        res = getCost(nums[0])
        
        while L<R:
            mid = (L+R)//2
            c1 = getCost(mid)
            c2 = getCost(mid+1)
            res = min(c1,c2)
            
            if c1>c2:
                L = mid +1 
            
            else:
                R = mid
            
        return res