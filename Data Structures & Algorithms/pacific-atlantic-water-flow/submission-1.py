class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_reachable = set()
        atlantic_reachable = set()

        m = len(heights)
        n = len(heights[0])

        def dfs(r, c, reachable, prev_height):
            if r < 0 or r >= m or c < 0 or c >= n:
                return

            if (r, c) in reachable:
                return

            if heights[r][c] < prev_height:
                return

            reachable.add((r, c))

            dfs(r + 1, c, reachable, heights[r][c])
            dfs(r - 1, c, reachable, heights[r][c])
            dfs(r, c + 1, reachable, heights[r][c])
            dfs(r, c - 1, reachable, heights[r][c])
            

        for i in range(n):
            dfs(0, i, pacific_reachable, heights[0][i])
            dfs(m-1, i, atlantic_reachable, heights[m-1][i])
        for i in range(m):
            dfs(i, 0, pacific_reachable, heights[i][0])
            dfs(i, n-1, atlantic_reachable, heights[i][n-1])

        return list(pacific_reachable & atlantic_reachable)
