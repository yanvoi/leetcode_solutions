class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        distinct = [string for string in count if count[string] == 1]
        return distinct[k - 1] if k <= len(distinct) else ""
