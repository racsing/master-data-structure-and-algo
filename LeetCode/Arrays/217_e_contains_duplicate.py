from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n) (hashset)
class Solution_1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


# Time Complexity: O(nlogn) (traversing + sort)
# Space Complexity: O(1)
class Solution_2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        result = False
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                result = True
        return result


solve = Solution_2()
nums_input = [1, 2, 3, 4, 1, 1]

output = solve.containsDuplicate(nums_input)
print(output)
