from typing import List


# Iteration Method
# TC: O(logn)
# SC: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


solve = Solution()
print(solve.search(nums=[2,5], target=5))
