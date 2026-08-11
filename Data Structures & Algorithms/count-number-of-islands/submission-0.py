class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c, grid):
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r+1, c, grid)
            dfs(r-1, c, grid)
            dfs(r, c+1, grid)
            dfs(r, c-1, grid)

        if not grid:
            return 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j, grid)

        return res