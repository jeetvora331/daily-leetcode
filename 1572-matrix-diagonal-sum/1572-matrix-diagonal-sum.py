class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0 
        n = len(mat)
        
        for i in range(n):
            res += mat[i][i]
            
            res += mat[i][n-i-1]
            
        if n%2 :
            res -= mat[n//2][n//2]
                
        return res
        