class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        answer = 0
        seen = set()
        for word in words:
            if word[::-1] in seen:
                answer += 1
            seen.add(word)

        return answer
