# Binary Search

class Solution:

    # Function to find minimum number of pages.
    def findPages(self, A, N, M):
        def isAllocationPossible(maxpages):
            stu, currentpages = 1, 0

            for i in range(N):
                if currentpages + A[i] > maxpages:
                    stu += 1
                    if stu > M:
                        return False
                    currentpages = A[i]
                else:
                    currentpages += A[i]
            return True

        # search space
        lo, hi = A[N - 1], sum(A)
        res = float('inf')

        # no of books is less than no of student
        # Each student has to be allocated at least one book.
        if N < M:
            return -1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if isAllocationPossible(mid):
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return res


N = 4
A = [12, 34, 67, 90]
M = 2
solve = Solution()
print(solve.findPages(A, N, M))

