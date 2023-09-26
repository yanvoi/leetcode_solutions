# O(n) time, O(n) space
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        left_sum = [0] * len(words)
        for i, word in enumerate(words):
            left_sum[i] = word[0] in vowels and word[-1] in vowels
            left_sum[i] += left_sum[i - 1] if i else 0

        return [left_sum[r] - left_sum[l - 1] if l else left_sum[r] for l, r in queries]
