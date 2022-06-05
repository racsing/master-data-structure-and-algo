from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = len(sentences[0].split())
        print(max_words)
        for words in sentences:
            tmp = words.split()
            print(tmp)
            if len(tmp) > max_words:
                max_words = len(tmp)
        return max_words


sentences = ["please wait", "continue to fight", "continue to win"]
solve = Solution()
max_words_count = solve.mostWordsFound(sentences)
print(max_words_count)
