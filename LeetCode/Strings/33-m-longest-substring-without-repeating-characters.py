# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                print(charSet, l)
                print("while end")
            charSet.add(s[r])
            res = max(res, r-l+1)
            print(charSet, res)
        return res


solve = Solution()
# input_str = "abcabcbb"
input_str = "pwwkew"
print(solve.lengthOfLongestSubstring(input_str))
