class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numOfProvinces=0
        visited=set()
        
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)
                    
        
        for start in range(len(isConnected)):
            if start not in visited:
                numOfProvinces+=1
                dfs(start)
                
        return numOfProvinces 