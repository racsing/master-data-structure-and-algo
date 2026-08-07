""" HINT
A really brute force way would be to search for all possible pairs of numbers but that would be too slow. Again,
it's best to try out brute force solutions for just for completeness. It is from these brute force solutions that you
can come up with optimizations. So, if we fix one of the numbers,
say x,
we have to scan the entire array to find the next number: y
which is: value - x
where value is the input parameter. Can we change our array somehow so that this search becomes faster?
The second train of thought is, without changing the array, can we use additional space somehow? Like maybe a hash map
 to speed up the search?
"""

from typing import List


class Solution:
    def two_sum_problem(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            else:
                seen[value] = i


solve = Solution()
num_list = [2, 4, 11, 5]
target_value = 9
print(solve.two_sum_problem(num_list, target_value))

