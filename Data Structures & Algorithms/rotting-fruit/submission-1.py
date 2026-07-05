class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        n = len(grid)
        m = len(grid[0])
        q = deque()
        fresh = 0
        minutes = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append([i,j])
        if fresh == 0:
            return 0
        

        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for a,b in ([i+1,j],[i,j+1],[i-1,j],[i,j-1]):
                    if 0<=a<n and 0<=b<m and grid[a][b]==1:
                        fresh-=1
                        grid[a][b]=2
                        q.append([a,b])
            minutes+=1
        if fresh > 0:
            return -1
        else:
            return minutes-1
