class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0] * len(pref)
        prev = 0
        for i, xor in enumerate(pref):
            arr[i], prev = prev ^ xor, xor

        return arr
