class Solution:
    # Function to check if two arrays are equal or not.
    def check(A, B, N):

        A.sort()
        B.sort()

        for i in range(N):
            if A[i] != B[i]:
                return False

        return True


N = 5
A = [1, 2, 5, 4, 0]
B = [2, 4, 5, 0, 1]
print(Solution.check(A, B, N))
