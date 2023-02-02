class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alphabet = {char: i for i, char in enumerate(order)}
        words = [[alphabet[char] for char in word] for word in words]

        return all(word1 <= word2 for word1, word2 in zip(words, words[1:]))
