class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [part for word in words for part in word.split(separator) if part]
