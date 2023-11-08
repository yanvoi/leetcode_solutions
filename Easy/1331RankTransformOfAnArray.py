class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = defaultdict(int)
        for i, num in enumerate(sorted(arr)):
            rank[num] = rank[num] if num in rank else len(rank) + 1
        return map(rank.get, arr)
