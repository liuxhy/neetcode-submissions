class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reachable = set()
        atlantic_reachable = set()

        m = len(heights)
        n = len(heights[0])

        def dfs(r,c, reachable):
            reachable.add((r,c))
            for (x,y) in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr, nc = r+x, c+y
                if nr < 0 or nr >=m or nc < 0 or nc >= n:
                    continue
                if (nr,nc) in reachable:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr,nc,reachable)
            

        for i in range(n):
            dfs(0, i, pacific_reachable)
            dfs(m-1, i, atlantic_reachable)
        for i in range(m):
            dfs(i, 0, pacific_reachable)
            dfs(i, n-1, atlantic_reachable)

        return list(pacific_reachable & atlantic_reachable)
