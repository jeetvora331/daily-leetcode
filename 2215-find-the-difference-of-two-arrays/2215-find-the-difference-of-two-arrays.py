class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x = []
        y = []
        
        for i in nums1:
            if i in nums2:
                continue 
            else:
                x.append(i)
        
        for j in nums2:
            if j in nums1:
                continue 
            else:
                y.append(j)
        
        return [list(set(x)) , list(set(y))]