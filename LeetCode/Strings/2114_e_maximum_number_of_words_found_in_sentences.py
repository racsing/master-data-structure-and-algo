from typing import List


class Solution_1:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = len(sentences[0].split())
        print(max_words)
        for words in sentences:
            tmp = words.split()
            print(tmp)
            if len(tmp) > max_words:
                max_words = len(tmp)
        return max_words

class Solution_2:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(word.split()) for word in sentences)

sentences = ["please wait", "continue to fight", "continue to win"]
solve = Solution_2()
max_words_count = solve.mostWordsFound(sentences)
print(max_words_count)
