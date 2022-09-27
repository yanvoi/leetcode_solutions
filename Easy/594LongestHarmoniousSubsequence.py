class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        count, res = dict(), 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
            if num - 1 in count:
                res = max(res, count[num - 1] + count[num])
            if num + 1 in count:
                res = max(res, count[num + 1] + count[num])
                
        return res
        
