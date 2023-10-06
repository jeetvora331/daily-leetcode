class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        bal = 0
        
        for sy in s:
            if sy == "(":
                bal +=1 
            else:
                bal -=1
            
            if bal == -1:
                ans +=1 
                bal +=1
                
        return ans + bal
        