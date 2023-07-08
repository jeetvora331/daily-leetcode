class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jwel = {}
        count = 0
        
        for i in jewels:
            jwel[i] = i
        
        for i in stones:
            if i in jwel:
                count +=1
                
        return count

        