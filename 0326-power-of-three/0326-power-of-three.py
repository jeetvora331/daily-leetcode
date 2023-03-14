class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Recurssive Solution
        
        while n>0 and n%3==0:
            return self.isPowerOfThree(n/3)
        
        return n==1
        
        
        
        
        
        # Iterative Solution
        
        if n<=0:
            return False
        
        while n%3 ==0:
            n = n / 3
        return n == 1
        
        
