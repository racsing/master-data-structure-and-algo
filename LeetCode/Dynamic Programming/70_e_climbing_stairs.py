class Solution_1:
    def climbStairs(self, n: int) -> int:
            if n == 1:
                return 1
            a, b = 1, 2
            for i in range(2, n):
                tmp = b
                b = a + b
                a = tmp
            return b


class Solution_2:
    def climbStairs(self, n: int) -> int:
        second_last, last = 1, 1
        temp = 1
        for i in range(n - 1):
            last += temp
            temp = second_last
            second_last = last
            print(second_last, last)

        return last


solve = Solution_1()
print(solve.climbStairs(4))