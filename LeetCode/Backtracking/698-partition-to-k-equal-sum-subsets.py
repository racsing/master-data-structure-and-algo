from typing import List


# [Solution 1] - DFS + Backtracking Solution, O(k^N) time (less optimal)
class Solution_1:
    def canPartitionKSubsets(nums: List[int], k: int) -> bool:
        total_sum, n = sum(nums), len(nums)
        visited = [False] * n

        if total_sum % k:
            return False

        target = total_sum // k
        nums.sort(reverse=True)

        # sorting the array in descending order
        # so if first value is greater than target, it will not be included in any subset
        # so we can't partition the entire array into k equal sum subsets

        if nums[0] > target:
            return False

        def backtrack(i, k, curSum):
            if k == 0: return True
            if target == curSum: return backtrack(0, k - 1, 0)

            for j in range(i, n):
                if not visited[j] and curSum + nums[j] <= target:
                    visited[j] = True
                    if backtrack(j + 1, k, curSum + nums[j]):
                        return True
                    visited[j] = False
            return False
        return backtrack(0, k, 0)


class Solution_2:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)  # Game Changer 1
        buck, kSum = [0] * k, sum(nums) // k

        def dfs(idx):
            if idx == len(nums): return len(set(buck)) == 1
            for i in range(k):
                buck[i] += nums[idx]
                if buck[i] <= kSum and dfs(idx + 1): return True
                buck[i] -= nums[idx]
                if buck[i] == 0: break  # Game Changer 2
            return False

        return dfs(0)


# Print Solution
print(Solution.canPartitionKSubsets(nums=[4, 3, 2, 3, 5, 2, 1], k=4))
