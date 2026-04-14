class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_islands = 0

        def dfs(row, col):
            # Move down
            if row + 1 < m and grid[row+1][col] == "1":
                grid[row+1][col] = "0"
                dfs(row+1, col)

            # Move up
            if row - 1 >= 0 and grid[row-1][col] == "1":
                grid[row-1][col] = "0"
                dfs(row-1, col)

            # Move left
            if col + 1 < n and grid[row][col+1] == "1":
                grid[row][col+1] = "0"
                dfs(row, col+1)

            # Move right
            if col - 1 >= 0 and grid[row][col-1] == "1":
                grid[row][col-1] = "0"
                dfs(row, col-1)

        i = 0
        while i < m:
            j = 0
            while j < n:
                print(grid[i][j])
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    num_islands += 1
                    # Perform DFS
                    dfs(i, j)
                j += 1

            i += 1

        return num_islands