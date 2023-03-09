class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x ,n):
            # Base Case
            if x == 0 : return 0
            if n == 0 : return 1
            
            # Recurrence Relation 
            res = helper(x*x , n//2)
            if n%2 == 1:
                return res * x 
            else:
                return res
        
        res = helper(x , abs(n))
        
        if n < 0:
            return 1/res
        else:
            return res
            