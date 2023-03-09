class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        res = 0
        for i , n in enumerate(s):
            
            if i + 1 < len(s) and hm[n] < hm [s[i+1]] :
                res -= hm[n]
            
            else:
                res += hm[n]
            
        return res