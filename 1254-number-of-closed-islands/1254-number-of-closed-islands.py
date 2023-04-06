class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        
        def dfs(r,c):
            if (r<0 or c<0 or r==rows or c==cols):
                return 0
            
            if grid[r][c] == 1 or (r,c) in visit:##
                return 1
            
            visit.add((r,c))
            curr = min(dfs(r+1,c), dfs(r,c+1),dfs(r-1,c),dfs(r,c-1))
            
            return curr
        
        res = 0
        for r in range(rows):
            for c in range(cols):
                if not grid[r][c] and (r,c) not in visit:
                    res += dfs(r,c)
                    
        return res