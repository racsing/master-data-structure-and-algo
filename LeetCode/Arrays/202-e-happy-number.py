"""
Approach 1: Detect Cycles with a HashSet

Time complexity :  O(243⋅3 + logn + loglogn + logloglogn)... = O(logn)
Space Complexity : O(logn)

Finding the next value for a given number has a cost of O(logn) because we are processing each digit in the number,
and the number of digits in a number is given by logn.

"""


class Solution_1:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        while n != 1:
            digits = [int(x) for x in str(n)]
            n = 0
            for d in digits:
                n += d ** 2

            if n in hashset:
                return False
            else:
                hashset.add(n)

            print(digits, n, hashset)

        return True


# Approach 1: Detect Cycles with a HashSet
class Solution_2:
    def isHappy(self, n: int) -> bool:

        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1


# Approach 2: Floyd's Cycle-Finding Algorithm
# Time complexity :  O(logn)
# Space Complexity : O(1)
class Solution_3:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1


solve = Solution_1()
# n = 19
print(solve.isHappy(n=19))
