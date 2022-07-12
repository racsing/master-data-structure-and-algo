class Solution:
    # Function to find equilibrium point in the array.
    def equilibriumPoint(A, N):

        if N == 1:
            return N

        l, r = 0, N - 1

        leftSum = 0
        rightSum = 0

        while l <= r:
            if leftSum == rightSum and l == r:
                return l + 1

            elif leftSum < rightSum:
                leftSum += A[l]
                l += 1

            else:
                rightSum += A[r]
                r -= 1
            print(l, r, leftSum, rightSum)

        return -1


# N = 42
# Arr = [4, 42, 27, 16, 28, 3, 4, 5, 9, 3, 31, 5, 5, 29, 10, 18, 35, 35, 33, 19, 41, 23, 8, 32, 9, 5, 8, 18, 35,
#        13, 6, 7, 6, 10, 11, 13, 37, 2, 25, 7, 28, 43]

N = 5
Arr = [1, 3, 5, 2, 2]

print("Solution ::")
print(Solution.equilibriumPoint(Arr, N))
