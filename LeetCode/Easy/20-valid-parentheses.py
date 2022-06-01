class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        brackets = {0: None, '(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                if stack == [0] or brackets[char] != stack.pop():
                    return False
            else:
                return False
        return stack == [0]


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