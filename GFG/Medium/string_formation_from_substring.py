# Not an optimized Solution
# Use KMP Algo to optimize

class Solution:
	def isRepeat(self, s):
		length = len(s)
		loop = int(length / 2)

		if length == 1:
			return 0
		elif length % 2 != 0:
			loop += 1

		for i in range(1, loop+1):
			text = s[:i]
			counts = s.count(text)
			#counts = sum(map(lambda j, i, s: 1 if text in s[j:j+i] else 0, text))
			period = int(-(-length // i))
			print(text, counts, period)

			if period == counts:
				return 1

		return 0


input_str = "ababab"
solve = Solution()
print(solve.isRepeat(input_str))