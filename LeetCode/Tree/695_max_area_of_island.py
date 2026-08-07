from typing import List

"""
Approach: Depth-First Search (Recursive)

If we are on a land square and explore every square connected to it 4-directionally recursively, 
then the total number of squares explored will be the area of that connected shape.

To ensure we don't count squares in a shape more than once, 
let's use SEEN to keep track of squares we haven't visited before. 

Time Complexity: O(R * C)
Space Complexity: O(R * C)

"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()

        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    (r, c) not in seen and grid[r][c]):
                return 0

            seen.add((r, c))

            return (1 + dfs(r + 1, c) + dfs(r - 1, c) +
                    dfs(r, c - 1) + dfs(r, c + 1))

        return max(dfs(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

solve = Solution()
print(solve.maxAreaOfIsland(grid))