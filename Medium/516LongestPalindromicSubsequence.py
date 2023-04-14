class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        self.s = s
        return self._dfs(0, len(s) - 1)


    @cache
    def _dfs(self, left, right):
        
        if left == right:
            return 1

        if left > right:
            return 0

        # these 2 characters will always be included in this subsequence's palindrome
        if self.s[left] == self.s[right]:
            return 2 + self._dfs(left + 1, right - 1)

        # either skip left or right character
        return max(self._dfs(left + 1, right), self._dfs(left, right - 1))
