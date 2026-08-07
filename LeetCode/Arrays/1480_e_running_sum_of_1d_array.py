from typing import List


# TC: O(n)
# SC: O(1)
class Solution_1:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            answer[i] += sum
            print(answer)
        return answer


# TC: O(n)
# SC: O(1)
class Solution_2:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            print(nums)
        return nums


input_nums = [1, 2, 3, 4]
solve = Solution_2()
print(solve.runningSum(input_nums))
