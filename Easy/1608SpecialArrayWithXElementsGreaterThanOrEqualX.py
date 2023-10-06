# O(nlogn) time, O(1) space
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        left, right = 1, len(nums)
        while left <= right:
            mid = (left + right) // 2
            count = sum(num >= mid for num in nums)
            if count == mid: return mid
            if count > mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1
