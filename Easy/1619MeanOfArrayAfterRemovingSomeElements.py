class Solution:
    def trimMean(self, arr: List[int]) -> float:
        return sum(sorted(arr)[len(arr) // 20: - len(arr) // 20]) / (len(arr) - 2 * (len(arr) // 20))
