class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        
        for r in range(n):
            for c in range(n):
                match = 1
                
                for i in range(n):
                    if grid[r][i] != grid[i][c]:
                        match = 0
                        break 
                count += match
        return count