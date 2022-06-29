# Binary Search
# Time Complexity: O(logN)
# Space Complexity: O(1)
from typing import List


class Solution_1:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if arr[mi] < arr[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
            print(lo, mi, hi)
        return lo


class Solution_2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            print(low, mid, high)
            if arr[mid - 1] < arr[mid] or mid == 0:
                if arr[mid] > arr[mid + 1] or mid + 1 == len(arr):
                    return mid
                else:
                    low = mid + 1
            else:
                high = mid - 1

        print(low, mid, high)
        return -1


solve = Solution_1()
print(solve.peakIndexInMountainArray(arr=[3, 9, 8, 6, 4]))
