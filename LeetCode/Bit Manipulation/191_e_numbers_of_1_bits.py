"""
TC: O(32) = O(1)
SC: O(1)

HINT: Doing an AND operation with the given N
suppose N = 11 = 1 0 1 '1'
               & 0 0 0  1
              -------------
           ans = 0 0 0 (0/1) => lsb bit of ans can be a zero or one depending on N-lsb bit
Then shift every bit and repeat the same

"""


class Solution:
    def hammingWeight(n: int) -> int:
        setBits = 0
        print(n)

        while n:
            setBits += n % 2
            n = n >> 1
            # print(n, setBits)

        return setBits


Solution.countbits()
print(Solution.hammingWeight(n=4294967293))
