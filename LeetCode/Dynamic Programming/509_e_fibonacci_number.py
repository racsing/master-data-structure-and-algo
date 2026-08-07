class Solution:
    def fibonacci(self, n: int) -> int:
        fibo = [0, 1]
        for i in range(2, n + 1):
            last = i - 1
            second_last = i - 2
            fibo.append(fibo[last] + fibo[second_last])
        print(fibo)
        return fibo[n]


solve = Solution()
print(solve.fibonacci(9))
