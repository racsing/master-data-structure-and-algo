class Solution:
    def fibonacci(self, n: int) -> int:
        f = [0, 1]
        for i in range(2, n + 1):
            last = i - 1
            second_last = i - 2
            f.append(f[last] + f[second_last])
        return f[n]


solve = Solution()
print(solve.fibonacci(9))
