class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        sr = 0
        er = len(mat) - 1 
        
        sc = 0
        ec = len(mat[0]) - 1
        
        while sr <= er and sc <= ec:
            for col in range(sc, ec + 1):
                res.append(mat[sr][col])
                
            for row in range(sr + 1, er + 1):
                res.append(mat[row][ec])
            
            if sr != er:
                for col in reversed(range(sc, ec)):
                    res.append(mat[er][col])
            
            if sc != ec:
                for row in reversed(range(sr + 1, er)):
                    res.append(mat[row][sc])
                
            sr += 1 
            er -= 1
            
            sc += 1
            ec -= 1
            
        return res
