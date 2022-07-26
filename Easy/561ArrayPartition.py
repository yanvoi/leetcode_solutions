class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        
        for el in nums[:len(nums)-1:2]:
            answer += el
            
        return answer
