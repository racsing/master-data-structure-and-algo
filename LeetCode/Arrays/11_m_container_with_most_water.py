from typing import List


# TWO POINTER SOLUTION

# TC: O(n) LINEAR TIME SOLUTION
# SC: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea


height_input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solve = Solution()
print(solve.maxArea(height_input))
