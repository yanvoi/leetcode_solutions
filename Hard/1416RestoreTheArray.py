class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        self.s = s
        self.k = k
        return self._dfs(0)

    
    @cache
    def _dfs(self, i):
        if i == len(self.s):
            return 1
        
        if self.s[i] == "0":
            return 0

        cur = 0
        num = 0
        for j in range(i + 1, len(self.s) + 1):
            num = 10 * num + int(self.s[j - 1])
            if num > self.k:
                break
            
            cur += self._dfs(j)

        return cur % (10 ** 9 + 7)
        
