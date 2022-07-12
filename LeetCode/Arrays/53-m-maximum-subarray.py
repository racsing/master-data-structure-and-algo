from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n
            maxSub = max(maxSub, curr_sum)
            print(n, curr_sum, maxSub)

        return maxSub


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solve = Solution()
print(solve.maxSubArray(nums))
