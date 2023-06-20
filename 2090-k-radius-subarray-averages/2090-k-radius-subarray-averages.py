class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        i = 0
        n = len(nums)
        average = [0] * n
        curr = 0
        
        while i < n:
            curr += nums[i]
            
            if i - k < 0 or i + k >= n:
                average[i] = -1
            
            if i>= 2*k:
                average[i-k] = curr //(2*k +1)
                curr -= nums[i-2*k]
            
            i+=1
        return average
    