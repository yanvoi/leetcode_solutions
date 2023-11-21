# O(n) time, O(1) space
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        same_prefix_count = 0
        for c1, c2, c3 in zip(s1, s2, s3):
            if c1 == c2 == c3: same_prefix_count += 1
            else: break

        return len(s1) + len(s2) + len(s3) - 3 * same_prefix_count if same_prefix_count else -1
