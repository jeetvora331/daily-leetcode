class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l=0
        r = len(matrix[0])
        b = len(matrix)
        t=0
        res = []
        
        while l<r and t<b:
            for i in range(l,r):
                res.append(matrix[t][i])
            t=t+1
                
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r = r-1
            
            if not (l<r and t<b):
                break
        
            for i in range(r-1,l-1,-1):
                res.append(matrix[b-1][i])
            b = b-1
                
            for i in range(b-1,t-1,-1):
                res.append(matrix[i][l])
                
            l= l+1
            
        return res
        
    
                    
        
        
        