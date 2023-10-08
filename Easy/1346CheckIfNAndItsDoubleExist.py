class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if (2 * num in seen) or (not num % 2 and num // 2 in seen): return True
            seen.add(num)

        return False
