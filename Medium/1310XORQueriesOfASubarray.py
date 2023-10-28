# O(n) time, O(n) space
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prev_xor, xors = 0, [0] * len(arr)
        for i, num in enumerate(arr):
            xors[i] = prev_xor ^ num
            prev_xor = xors[i]

        return [xors[right] ^ xors[left - 1] if left else xors[right] for left, right in queries]
