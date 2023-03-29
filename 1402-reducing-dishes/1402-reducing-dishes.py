class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort()
        res = 0 
        curr = 0

        while s and s[-1] + curr >0:
            curr = curr + s.pop()
            res += curr
        return res