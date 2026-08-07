from typing import List


class Solution:
    def findMin_2(self, nums: List[int]) -> int:
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1

    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        ans = nums[0]

        while low <= high:
            if nums[low] < nums[high]:
                ans = min(ans, nums[low])
                break
            mid = low + (high - low) // 2
            ans = min(ans, nums[m])
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1

        return ans


solve = Solution()
print(solve.findMin(nums=[11, 13, 15, 17]))
# [3,4,5,1,2]  [2,3,4,5,1] [1,2,3,4,5]
