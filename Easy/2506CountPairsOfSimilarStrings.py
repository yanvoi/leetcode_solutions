class Solution:
    def similarPairs(self, words: List[str]) -> int:
        answer = 0
        count = Counter()
        for word in words:
            bit_mask = 0
            for letter in word:
                index = ord(letter) - ord('a')
                bit_mask |= 1 << index

            answer += count[bit_mask]
            count[bit_mask] += 1

        return answer
