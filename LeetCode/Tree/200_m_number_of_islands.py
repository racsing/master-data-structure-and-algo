from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            if i < 0 or i > ROWS - 1 or \
               j < 0 or j > COLS - 1 or \
               (i, j) in visited or grid[i][j] == '0':
                return 0

            visited.add((i, j))

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        count = 0
        for i in range(ROWS):
            for j in range(COLS):

                if (i, j) not in visited and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
solve = Solution()
print(solve.numIslands(grid))
