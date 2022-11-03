class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        frequency = dict()
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
            
        answer = 0
        for num, val in frequency.items():
            if val == 1: answer += num
                
        return answer
        
