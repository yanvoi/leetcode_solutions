# O(n + m) time where n == len(target) && m == len(arr)
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return Counter(target) == Counter(arr)
