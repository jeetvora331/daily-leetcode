class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        bucket  = [0 for i in range(101)]
        
        for i in nums:
            bucket[i] += 1
        for idx in range(1,(len(bucket))):
            bucket[idx] += bucket[idx-1]
            
        res = []
        for i in nums:
            if i ==0:
                res.append(0)
            else:
                
                a = bucket[i -1]
                res.append(a)
        return res
            

        
        