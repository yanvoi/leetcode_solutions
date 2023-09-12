class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        return max([num for num in arr if num == counter[num]] + [-1])
