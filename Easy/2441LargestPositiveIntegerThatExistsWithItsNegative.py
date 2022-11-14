class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        s = set()
        contenders = [-1]
        
        for num in nums:
            if num * -1 in s:
                contenders.append(abs(num))
            s.add(num)
            
        return max(contenders)
        
