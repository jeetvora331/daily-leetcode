class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # very bad question
        i = 1
        s = "0"
        hmap = {"1":"0" , "0" : "1"}
        
        for i in range(1,n):
            rev ="" 
            for i in s:
                rev += hmap[i]
            rev = rev[::-1]
            
            s = s + "1" + rev
        
        return s[k-1]