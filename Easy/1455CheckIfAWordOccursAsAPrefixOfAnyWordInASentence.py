class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        for index, word in enumerate(sentence.split()):
            if word[:n] == searchWord: return index + 1

        return -1
