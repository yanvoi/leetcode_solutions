class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        self.subsequences = set()
        self.nums = nums
        self.dfs(0, [])
        return list(self.subsequences)

    
    def dfs(self, i, path):
        if i == len(self.nums):
            if len(path) >= 2:
                self.subsequences.add(tuple(path))
            return

        if not path or path[-1] <= self.nums[i]:
            path.append(self.nums[i])
            self.dfs(i + 1, path)
            path.pop()

        self.dfs(i + 1, path)
