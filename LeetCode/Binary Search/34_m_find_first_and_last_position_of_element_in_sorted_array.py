from typing import List


# Two Binary Search for First and Last element
# TC: O(N)
# SC: O(1)

class Solution:
    def searchRange(nums: List[int], target: int) -> List[int]:
        def helperFunc(nums, target, isfirst):
            lo, hi = 0, len(nums) - 1
            ans = -1

            # Find First & Last Occurrence of target
            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if nums[mid] == target:
                    if isfirst:
                        hi = mid - 1
                    else:
                        lo = mid + 1
                    ans = mid

                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return ans

        # Function call
        start = helperFunc(nums, target, isfirst=True)

        end = helperFunc(nums, target, isfirst=False)

        return [start, end]


print(Solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
