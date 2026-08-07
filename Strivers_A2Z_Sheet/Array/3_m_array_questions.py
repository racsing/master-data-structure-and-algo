"""
Array Medium Problems Practice
=============================

This file contains solutions for common medium-level array problems from A2Z Strivers Sheet.

Total Questions: 7

1. Two Sum
2. Sort Colors (three-pointer approach)
3. Sort Colors (counting approach)
4. Majority Element (Moore voting approach)
5. Majority Element (hash map approach)
6. Longest Subarray with Sum K (two-pointer approach)
7. Longest Subarray with Sum K (prefix-sum approach)
8. Maximum Subarray (Kadane's algorithm)
9. Maximum Subarray (extended version)
10. Rearrange Array
11. Leaders in an Array

Note: Multiple solution methods for the same question are counted as one question.
"""

class Solution:

    def two_sum(self, nums, target):
        """Given an array of integers nums and an integer target, 
        return indices of the two numbers such that they add up to target.
        TC: O(N), SC: O(N)
        """
        seen = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in seen and seen[ans] != i:
                return [seen[ans], i]
            seen[nums[i]] = i
        return []
    
    def sort_colors_pointers_optimal(self, nums):
        """Given an array nums consisting of only 0, 1, or 2.
        Sort the array in non-decreasing order and in-place.
        Approach: 3 pointers
        TC: O(N), SC: O(1)
        """
        l, mid, r = 0, 0, len(nums)-1
        while mid <= r:
            print(nums, l, mid, r)

            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                l += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1
        print(nums, l, mid, r)

    def sort_colors_counting_optimal(self, nums):
        """Given an array nums consisting of only 0, 1, or 2.
        Sort the array in non-decreasing order and in-place.
        Approach: Counting
        TC: O(N), SC: O(1)
        """
        count = [0] * 3
        for n in nums:
            count[n] += 1
        print("count: ", count)
        
        nums[:] = [0] * count[0] + [1] * count[1] + [2] * count[2]
        print("nums: ", nums)

    def majority_element_optimal(self, nums):
        """Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than ⌊n / 2⌋ times. 
        TC: O(N), SC: O(1)
        """
        majority = 0
        counter = 0
        for num in nums: 
            if counter == 0:
                majority = num
                counter = 1
            elif num == majority:
                counter += 1
            else:
                counter -= 1
            print(majority, counter, num)

    def majority_element_better(self, nums):
        """Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than ⌊n / 2⌋ times.
        TC: O(N), SC: O(N)
        """
        n = len(nums)
        majority = {}
        
        for num in nums:
            if num in majority:
                majority[num] += 1
            else:
                majority[num] = 1

        for num, count in majority.items():
            if count > n // 2:
                return num
        return -1

    def longest_subarray_with_sum_K_optimal(self, nums, k):
        """Given an array nums of size n and an integer k, 
        find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
        
        Approach: Two-Pointer / Sliding Window technique (positive numbers only)
        Time Complexity: O(N); Space Complexity: O(1) 
        """
        maxLength = 0
        currentSum = 0
        left = 0

        for right in range(len(nums)):
            currentSum += nums[right]

            while currentSum > k and left <= right:
                currentSum -= nums[left]
                left += 1
                if  currentSum == k:
                    maxLength = max(maxLength, right-left+1)
            
            print(f'maxLength={maxLength}, currentSum={currentSum}, j={left}, i={right}')

    def longest_subarray_with_sum_K_better(self, nums, k):
        """Given an array nums of size n and an integer k, 
        find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
        
        Approach: Using Hash Map and Prefix Sum (Positive + Negative numbers)
        Time Complexity: O(N); Space Complexity: O(N) 
        """
        maxLength = 0
        curSum = 0
        seen = {}
        # [10, 5, 2, 7, 1, 9]

        for i in range(len(nums)):
            curSum += nums[i]
            target = curSum - k

            if curSum == k:
                maxLength = max(maxLength, i+1)

            if target in seen:
                maxLength = max(maxLength, i-seen[target])
            
            if curSum not in seen:
                seen[curSum] = i
         
            print(f'maxLength={maxLength}, curSum={curSum}, target={target}, seen={seen} i={i}')

    def max_subarray_optimal(self, nums):
        """Given an integer array nums, find the subarray with the largest sum, and return its sum.
        Approach: Kadane's Algo
        TC: O(N); SC: O(1)
        """
        maxi = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            maxi = max(maxi, sum)
            if sum < 0:
                sum = 0
            print(nums, nums[i], sum, maxi)
        print("Largest sum: ", maxi)

    def max_subarray_extended(self, nums):
        """ Print subarray with maximum subarray sum (extended version of above problem)
        Approach: Kadane's Algo
        TC: O(N); SC: O(1)
        """
        maxi = float('-inf')
        sum = 0
        l, r = 0, -1
        for i in range(len(nums)):
            sum += nums[i]
            if sum == 0:
                l = i
            if sum > maxi:
                maxi = sum
                r = i
            if sum < 0:
                sum = 0
            print(nums, nums[i], sum, maxi)

        print("Largest sum: ", maxi, l, r)
        print("Subarray: ", nums[l:r+1])
    
    def rearrange_array_optimal(self, nums):
        """There's an array with an equal number of positive and negative elements. 
        Without altering the relative order of positive and negative elements, 
        you must return an array of alternately positive and negative values starting with positive always.
         TC: O(N); SC: O(N)
        """
        ans = [0] * len(nums)
        p, n = 0, 1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans[p] = nums[i]
                p += 2
            else:
                ans[n] = nums[i]
                n += 2
        print(ans)

    def leader_in_array(self, nums):
        """ Leaders in an Array only when all rightmost elements are smaller.
        TC: O(N); SC: O(1)
        """
        maxi = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= maxi:
                maxi = max(maxi, nums[i])
                print(f'{nums[i]} is a leader')
            




if __name__ == "__main__":

    solve: Solution = Solution()
    # print(solve.two_sum([2,7,11,15], 9))
    # solve.sort_colors_pointers_optimal([2,0,2,1,1,0])
    # solve.sort_colors_counting_optimal([0,0,2,1,1,0])
    # solve.majority_element_optimal([6,5,5])
    # solve.longest_subarray_with_sum_K_optimal([-3, 2, 1], k = 6)
    # solve.longest_subarray_with_sum_K_better([10, 5, 2, 7, 1, 9], k = 15)
    # solve.max_subarray_optimal([2, 3, 5, -2, 7, -4])
    # solve.max_subarray_extended([2, 3, 5, -2, -7, -7])
    # solve.rearrange_array_optimal([1,2,3,-1,-2,-3])
    solve.leader_in_array([10, 22, 12, 3, 0, 6] )


    



            