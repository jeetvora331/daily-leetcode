class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        stack = [] # [i , t]
        
        for i in reversed(range(len(nums))): 
            
            while stack and  nums[i] >= stack[-1][1]:
                stack.pop()
                
            if stack:
                res[i] = stack[-1][0] - i
                
            stack.append([i , nums[i]])
            
        return res
            