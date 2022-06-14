class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)

        dp = [[0 for _ in range(l1+1)] for _ in range(l2+1)]

        # Base Case
        for c in range(l1+1):
            dp[0][c] = c
        # Base Case
        for r in range(l2+1):
            dp[r][0] = r

        # 1 to 9, 1 to 5
        for i in range(1, l2+1):
            for j in range(1, l1+1):

                if word1[j-1] != word2[i-1]:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
                else:
                    dp[i][j] = dp[i-1][j-1]

        # Printing
        # for i in range(l2+1):
        #     for j in range(l2+1):
        #         print(dp[i][j], end=' ')
        #     print()

        return dp[-1][-1]


word1 = "leetcode"
word2 = "etco"
solve = Solution()
print(solve.minDistance(word1, word2))