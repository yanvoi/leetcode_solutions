# O(n^2) time, O(1) space
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels, answer = set("aeiou"), 0
        for i in range(len(s)):
            vowel_count, consonant_count = 0, 0
            for j in range(i, len(s)):
                vowel_count += s[j] in vowels
                consonant_count += s[j] not in vowels
                answer += vowel_count == consonant_count and not (vowel_count * consonant_count) % k

        return answer
