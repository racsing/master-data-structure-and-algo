# Quick sort
from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        L, M = len(left), len(mid)

        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L + M:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]


input_nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
input_k = 4
solve = Solution()
print(solve.findKthLargest(input_nums, input_k))
