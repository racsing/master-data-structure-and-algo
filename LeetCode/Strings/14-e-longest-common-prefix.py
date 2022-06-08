from typing import List
#
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         first_str = strs[0]
#
#         if len(strs) <= 1:
#             return first_str
#
#         l = len(first_str)
#         res = ""
#         for i in range(l):
#             for j in range(i + 1, l + 1):
#                 substring = first_str[i:j]
#                 print(i,j,substring)
#                 m = 0
#                 for k in range(1, len(strs)):
#                     if substring in strs[k]:
#                         m += 1
#                 if m == len(strs) - 1 and len(substring) > len(res):
#                     res = substring
#
#         return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        # find shortest len so no index out of range error
        lens = [len(str) for str in strs]
        min_len = min(lens)
        result = ''
        
        for i in range(1, min_len + 1):
            prefix = strs[0][:i]
            for s in strs:
                if s[:i] != prefix:
                    return result
            result = prefix

        return result


solve = Solution()
strs = ["ab", "a"]
print("Result = " + solve.longestCommonPrefix(strs))
