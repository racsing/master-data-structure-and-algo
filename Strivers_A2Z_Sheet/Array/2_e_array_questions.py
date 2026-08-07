"""
Array Easy Problems Practice
============================

This file contains solutions for common easy-level array problems from A2Z Strivers Sheet.

Total Questions: 8

1. Largest Element
2. Second Largest Element
3. Check if Array is Sorted
4. Remove Duplicates from Sorted Array
5. Rotate Array (with extra space)
6. Rotate Array (optimal in-place)
7. Move Zeroes
8. Find Maximum Consecutive Ones
9. Single Number

Note: Multiple solution methods for the same question are counted as one question.
"""

class Solution:
    def largest_element(self, nums):
        """ Given an array of integers nums, return the value of the largest element in the array
        Time Complexity: O(N); Space Complexity: O(1)
        """
        large = nums[0]
        for n in nums:
            if large < n:
                large = n
        print(f'Largest element in the array: {nums} is "{large}"')

    def second_largest_element(self, nums):
        """ Given an array of duplicate integers, return the second-largest element in the array. 
        If the second-largest element does not exist, return -1.
        Time Complexity: O(N); Space Complexity: O(1)
        """
        first = second = -1
        for n in nums:
            if first < n:
                second = first
                first = n
            elif second < n and n != first:
                second = n
        print(f'Second Largest element in the array: {nums} is "{second}"')

    def is_sorted(self, arr, n):
        """ Given an array of size n, If the array is sorted then return True, Else return False.
        Time Complexity: O(N); Space Complexity: O(1)        
        """
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True

    def remove_duplicates(self, nums):
        """Given an integer array sorted in non-decreasing order, 
        remove the duplicates in place such that each unique element appears only once. 
        The relative order of the elements should be kept the same. 
        If there are k elements after removing the duplicates, 
        then the first k elements of the array should hold the final result. 
        It doesn't matter what you leave beyond the first k elements.
        
        Time Complexity: O(N); Space Complexity: O(1) 
        """
        k = 0
        print(k, nums)
        for i in range(1, len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
                print(k, nums, i)
        print(k, nums)

    def rotate_array_better(self, nums, k):
        """ Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
         Time Complexity: O(N); Space Complexity: O(N) 
        """
        n = len(nums)
        tmp = [0] * n
        for i in range(n-1, -1, -1):
            tmp[(i+k)%n] = nums[i]
            print(tmp, (i+k)%n, i)
        nums = tmp
        print("nums", nums)

    def rotate_array_optimal(self, nums, k):
        """ Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
        Time Complexity: O(N); Space Complexity: O(1) 
        """
        n = len(nums)
        k = k % n

        # Reverse the whole array: (0 -> n-1)
        l, r = 0, n-1
        while(l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        
        # Reverse first k elements: (0 -> k-1)
        l, r = 0, k-1
        while(l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        
        # Reverse last k elemnts: (k -> n-1)
        l, r = k, n-1
        while(l < r):
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

        print(nums)

    def move_zeroes(self, nums):
        """ Given an integer array nums, move all 0's to the end of it 
        while maintaining the relative order of the non-zero elements and in-place.
        Time Complexity: O(N); Space Complexity: O(1) 
        """
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        for i in range(n-k):
            nums[i+k] = 0
            print(nums, k, i)
        print(nums)

    def find_max_consecutive_ones(self, nums):
        """Given a binary array nums, return the maximum number of consecutive 1's in the array.
        Time Complexity: O(N); Space Complexity: O(1) 
        """
        k = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
               k += 1
               maxi = max(maxi, k)
            else:
                k = 0
        print(maxi)

    def single_number(self, nums):
        """Given a non-empty array of integers nums, every element appears twice except for one. 
        Find that single one. 
        Time Complexity: O(N); Space Complexity: O(1) 
        """
        xorr = 0
        for i in range(len(nums)):
            xorr ^= nums[i]
        print(xorr)


if __name__ == "__main__":
    nums = [3, 3, 6, 1]
    nums2 = [3, 3, 0, 99, -40]
    nums3 = [7, 7, 2, 2, 10, 10, 10]
    nums4 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    arr = [1, 4, 4, 4, 9]

    solve: Solution = Solution()
    solve.largest_element(nums2)
    solve.second_largest_element(nums3)
    print(solve.is_sorted(arr, len(arr)))
    solve.remove_duplicates(nums4)
    solve.rotate_with_extra_space([1,2,3,4,5,6,7], 3)
    solve.rotate_array([1,2,3,4,5,6,7], 3)
    solve.move_zeroes([0,1,0,3,12])
    solve.find_max_consecutive_ones([1,1,0,1,1,1])
    solve.single_number([4,1,2,1,2])



            