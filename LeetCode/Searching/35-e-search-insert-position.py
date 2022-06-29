from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            print(low, mid, high)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            print(low, mid, high)
            print(nums[mid], target)
        return low


solve = Solution()
print(solve.searchInsert(nums=[1, 3, 5, 6], target=5))
