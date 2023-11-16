class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        to_swap = (sum(aliceSizes) - sum(bobSizes)) // 2
        alices = set(aliceSizes)
        for bob in bobSizes:
            if to_swap + bob in alices:
                return [to_swap + bob, bob]
