from typing import List


# If nums is empty, we return 0. Otherwise, Initialize length = 1, which is the length of the sorted array without
# duplicates. Initialize two pointers i = 0, j = 1. Iterate j over range(1, len(nums)), and if nums[j] != nums[i],
# we increment i by 1, and swap nums[i] and nums[j]. It is easy to see the loop invariant that nums[:i+1] is always
# the sorted array nums[:j+1] with duplicates removed. Hence, when j reaches len(nums)-1, nums[:i+1] is nums with
# duplicates removed.
#
# Time complexity: O(n), space complexity: O(1).
class Solution_1:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 1
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
                length += 1
                print(f'i = {i}, j = {j}, length = {length}')
                print("nums = " + str(nums))
        print("value = " + str(nums))
        return length


# To improve performance, get rid of index() and use set data structure instead
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(set(nums))
        nums.sort()
        print(nums)
        return len(nums)


nums = [1, 1, 1, 2, 2, 3, 4, 4]
solve = Solution_1()
pos = solve.removeDuplicates(nums)
print(pos)
