class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [index for index, word in enumerate(words) if x in word]
