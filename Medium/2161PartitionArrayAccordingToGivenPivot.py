class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        smaller = [num for num in nums if num < pivot]
        greater = [num for num in nums if num > pivot]
        return smaller + [pivot] * nums.count(pivot) + greater
