# Quick Select
#
from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pivot = random.choice(nums)
        greater = [x for x in nums if x > pivot]
        equal = [x for x in nums if x == pivot]
        lesser = [x for x in nums if x < pivot]

        print(pivot, greater, equal, lesser)

        G, E = len(greater), len(equal)
        print(k, G, E)
        if k <= G:
            return self.findKthLargest(greater, k)
        elif k > G + E:
            return self.findKthLargest(lesser, k - G - E)
        else:
            return equal[0]


input_nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
input_k = 4
solve = Solution()
print(solve.findKthLargest(input_nums, input_k))
