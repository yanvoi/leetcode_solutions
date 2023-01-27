class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        self.available = set(words)
        result = []
        for word in words:
            if self.dfs(word):
                result.append(word)

        return result


    @cache
    def dfs(self, word):

        for i in range(1, len(word)):

            prefix = word[:i]
            suffix = word[i:]

            if prefix in self.available and suffix in self.available:
                return True

            if prefix in self.available and self.dfs(suffix):
                return True

        return False
