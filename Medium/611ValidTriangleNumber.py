class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        
        for k in range(len(nums)):
            i = 0
            j = k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    answer += j - i
                    j -= 1
                else:
                    i += 1
        
        return answer
