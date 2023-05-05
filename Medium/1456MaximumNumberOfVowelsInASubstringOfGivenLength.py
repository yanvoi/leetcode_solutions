# O(n) time complexity - sliding window
class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set(('a', 'e', 'i', 'o', 'u'))
        cur_vowels_count = sum(char in vowels for char in s[:k])
        answer = cur_vowels_count

        for i in range(k, len(s)):
            cur_vowels_count -= s[i - k] in vowels
            cur_vowels_count += s[i] in vowels
            answer = max(answer, cur_vowels_count)

        return answer
