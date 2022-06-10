# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
            # print(prefix, answer[i])

        for j in range(len(nums) - 1, -1, -1):
            # print(answer)
            answer[j] *= postfix
            postfix *= nums[j]
            # print(postfix, answer[j])

        return answer


solve = Solution()
input_nums = [1, 2, 3, 4]
print(solve.productExceptSelf(input_nums))
