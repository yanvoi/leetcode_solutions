# O(n) time, O(n) space
class Solution:
    def numSplits(self, s: str) -> int:
        left, right = [0] * len(s), [0] * len(s)
        unique_left, unique_right = set(), set()
        for i in range(len(s)):
            unique_left.add(s[i])
            left[i] = len(unique_left)
            unique_right.add(s[-i - 1])
            right[-i - 1] = len(unique_right)

        return sum(left == right for left, right in zip(left, right[1:]))
