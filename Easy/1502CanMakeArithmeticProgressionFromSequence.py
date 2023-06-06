class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()
        return all(n3 - n2 == n2 - n1 for n1, n2, n3 in zip(arr, arr[1:], arr[2:]))
