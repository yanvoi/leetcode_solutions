# O(n) time, O(1) space, brilliant (because simple) solution by lee215
# two pointers, start from the middle (k), expand greedily left or right
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        answer = cur_min = nums[k]
        i = j = k
        while 0 < i or j < len(nums) - 1:
            if (nums[i - 1] if 0 <= i - 1 else 0) > (nums[j + 1] if j + 1 < len(nums) else 0): i -= 1
            else: j += 1
            cur_min = min(cur_min, nums[i], nums[j])
            answer = max(answer, cur_min * (j - i + 1))

        return answer
