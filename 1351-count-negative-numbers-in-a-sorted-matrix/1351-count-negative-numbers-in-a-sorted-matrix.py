class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        for row in grid:
            L = 0
            R = n-1
            
            while L <=R:
                mid = (L+R)//2
                if row[mid] < 0:
                    R = mid -1
                else:
                    L = mid +1
            count += n-L
            
        return count
                