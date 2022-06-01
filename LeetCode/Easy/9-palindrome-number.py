"""
        Special cases:
        when x < 0, x is not a palindrome.
        Also if the last digit of the number is 0, in order to be a palindrome,
        the first digit of the number also needs to be 0.
        Only 0 satisfy this property.

        When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        For example when the input is 12321, at the end of the while loop we get x = 12, reverse_num = 123,
        since the middle digit doesn't matter in palindrome(it will always equal to itself), we can simply get rid of it.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_num = 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        while x > reverse_num:
            reverse_num = (reverse_num * 10) + (x % 10)
            x = x // 10

        return True if (x == reverse_num or x == reverse_num // 10) else False


solve = Solution()
value = solve.isPalindrome(-121)
print(value)

