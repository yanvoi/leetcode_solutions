class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        self.word1, self.word2 = word1, word2
        self.l1, self.l2 = len(word1), len(word2)
        return self.edit(0, 0)

    
    @cache
    def edit(self, i, j):

        # we've reached the end of both words
        if i == self.l1 and j == self.l2:
            return 0
        
        # we've reached the end of the first word - delete all 'hanging' chars from the second word
        if i == self.l1:
            return self.l2 - j

        # we've reached the end of the second word - delete all 'hanging' chars from the first word
        if j == self.l2:
            return self.l1 - i

        # characters at these indices are the same - we check the next positions
        if self.word1[i] == self.word2[j]:
            return self.edit(i + 1, j + 1)

        # execute all possible actions and return whichever is the best
        insert = 1 + self.edit(i, j + 1)
        delete = 1 + self.edit(i + 1, j)
        replace = 1 + self.edit(i + 1, j + 1)

        return min(insert, delete, replace)
