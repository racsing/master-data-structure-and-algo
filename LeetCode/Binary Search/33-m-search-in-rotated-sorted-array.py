from typing import List


class Solution:
    def search(nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            # left sorted part
            if nums[l] <= nums[mid]:
                if nums[mid] <= target or nums[l] > target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


print(Solution.search(nums=[4, 5, 6, 7, 8, 1, 2, 3], target=8))
