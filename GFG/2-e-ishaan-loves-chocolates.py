# TWO POINTER ALGORITHM

# TC: O(N)
# SC: O(1)
class Solution:
    def chocolates(self, array, n):
        minimum = array[0]
        for i in range(1, n):
            minimum = min(minimum, array[i])

        return minimum


input_array = [5, 9, 2, 6]
length = len(input_array)

solve = Solution()
print(solve.chocolates(input_array, length))

