# Complexity: O(n), where n = len of input string

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {"]": "[", "}": "{", ")": "("}
        for char in s:
            if char in dictionary.values():
                stack.append(char)
            elif char in dictionary.keys():
                if stack == [] or dictionary[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


solve = Solution()
result = solve.isValid("([}}])")
print(result)


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         res = False
#         if len(s) % 2 != 0:
#             res = False
#             return res
#         open_brackets = ['[', '(', '{']
#         for char in s:
#             if char in open_brackets:
#                 stack.append(char)
#             elif char == ')' and stack != []:
#                 if '(' == stack[-1]:
#                     stack.pop()
#             elif char == ']' and stack != []:
#                 if '[' == stack[-1]:
#                     stack.pop()
#             elif char == '}' and stack != []:
#                 if '{' == stack[-1]:
#                     stack.pop()
#         res = True if not stack else False
#         return res