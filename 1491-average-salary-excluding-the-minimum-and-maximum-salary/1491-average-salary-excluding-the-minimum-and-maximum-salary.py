class Solution:
    def average(self, s: List[int]) -> float:
        # res = sum(s) - max(s) -min(s)
        # return res/(len(s) - 2)
        curr = 0
        currMin = float("inf")
        currMax = float("-inf")
        for i in range(len(s)):
            curr += s[i]
            if s[i] < currMin:
                currMin = s[i]
            if s[i] > currMax:
                currMax = s[i]
        
        res = curr - currMin - currMax
        return res/(len(s) -2)
            
             
        