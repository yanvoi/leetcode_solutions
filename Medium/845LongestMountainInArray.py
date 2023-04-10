# O(n) time using dynamic programming
# record lengths of streaks of sorted subarrays
# find a peak with longest streaks from both sides
class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        dp_left, dp_right = [0] * len(arr), [0] * len(arr)
        for i in range(1, len(arr), 1):
            if arr[i - 1] < arr[i]:
                dp_left[i] = dp_left[i - 1] + 1
        
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                dp_right[i] = dp_right[i + 1] + 1

        answer = 0
        for left, right in zip(dp_left, dp_right):
            if left >= 1 and right >= 1:
                answer = max(answer, left + right + 1)

        return answer
