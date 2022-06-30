from typing import List
import bisect


class Solution:
    # SOLUTION 3 :: Two Pointer
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        i = 0
        j = 0
        dist = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] >= arr2[j]:
                if arr1[i] - arr2[j] > d:
                    j += 1
                else:
                    i += 1
            else:
                if arr2[j] - arr1[i] > d:
                    i += 1
                    dist += 1
                else:
                    i += 1
        dist += len(arr1) - i
        return dist


"""
    SOLUTION 2 :: Binary Search
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        arr2.sort()
        for num in arr1:
            index = bisect.bisect_left(arr2, num)
            min_dist = float('inf')
            if index > 0:
                min_dist = min(min_dist, abs(num - arr2[index-1]))
            if index < len(arr2):
                min_dist = min(min_dist, abs(num - arr2[index]))
            if min_dist > d:
                ans += 1
        return ans

==================

    SOLUTION 1 ::  Brute Force
    TC: O(N^2) 
    SC: O(1)
        def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
            distance = len(arr1)

            for i in arr1:
                for j in arr2:
                    if abs(i-j) <= d:      
                        distance -= 1
                        break
            return distance
"""

solve = Solution()
print(solve.findTheDistanceValue(arr1=[5, 4, 8, 11], arr2=[10, 9, 1, 8], d=2))
