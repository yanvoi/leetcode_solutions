# great solution by lee215
# https://leetcode.com/problems/maximum-width-ramp/solutions/208348/
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        answer = 0
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            # only push elements greater than the ones we've already seen
            # no need for pushing repeating elements because we care for the right most one 
            if not stack or nums[i] > stack[-1][0]:
                stack.append((nums[i], i))
            
            # get index of the smallest greater (or equal) element
            j = stack[bisect.bisect_left(stack, (nums[i], i))][1]
            answer = max(answer, j - i)

        return answer
