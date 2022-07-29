class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if len(nums) == 0:
            return []
        
        start = 0
        finish = 0
        answer = []
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                if start == finish:
                    answer.append(str(nums[finish]))
                else:
                    answer.append(str(nums[start])+"->"+str(nums[finish]))
                start = i
                finish = i
            else:
                finish += 1
                
        if start == finish:
            answer.append(str(nums[finish]))
        else:
            answer.append(str(nums[start])+"->"+str(nums[finish]))
                
        return answer
            
