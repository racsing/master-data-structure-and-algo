# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l, r, Total = 0, 0, 0
        findSum = sum(nums) - x

        for i in range(len(nums) + 2):
            if Total > findSum:
                Total -= nums[l]
                l += 1
            elif Total == findSum:
                maxLen = r - l
                minOps = len(nums) - maxLen
                if minOps > maxLen:
                    Total -= nums[l]
                    l += 1
                else:
                    return minOps
            else:
                Total += nums[r]
                r += 1

        return -1


input_nums = [5,6,7,8,9]
input_x = 4
solve = Solution()
print(solve.minOperations(input_nums, input_x))
