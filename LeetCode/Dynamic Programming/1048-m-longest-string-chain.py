# SORT, MEMOIZATION,

from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())


input_words = ["a", "b", "ba", "bca", "bda", "bdca"]

solve = Solution()
print(solve.longestStrChain(input_words))