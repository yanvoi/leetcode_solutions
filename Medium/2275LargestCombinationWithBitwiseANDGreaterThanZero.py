class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        ones_on_bit = defaultdict(int)
        for candidate in candidates:
            candidate_binary = format(candidate, "b")[::-1]

            for i, digit in enumerate(candidate_binary):
                ones_on_bit[i] += int(digit)

        return max(ones_on_bit.values())
