

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [[0,1], [0,-1], [1,0] , [-1,0]]
        
        def invalid(r,c):
            return r<0 or c<0 or r== N or c ==N
        
        visited = set()
        
        def dfs(r,c):
            if (invalid(r,c) or not grid[r][c] or (r,c) in visited):
                return
            
            visited.add((r,c))
            for dr , dc in direct:
                dfs(r+dr , c + dc)
                
            return None
        
        def bfs():
            res = 0
            q = deque(visited)
            
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    
                    for dr , dc in direct:
                        currR = r+ dr
                        currC = c+ dc
                        
                        if invalid(currR , currC) or (currR , currC) in visited:
                            continue
                        
                        if grid[currR][currC]:
                            return res
                        q.append([currR, currC])
                        visited.add((currR, currC))
                res +=1
                        
            return -1
            
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()
