class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations_count, elements = 0, set()
        for num in nums[::-1]:
            operations_count += 1
            if num <= k: elements.add(num)
            if len(elements) == k: return operations_count

        return -1
