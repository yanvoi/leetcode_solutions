class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        h = dict()
        for el in nums:
            if el in h:
                h[el] += 1
            else:
                h[el] = 1
                
        degree = max(h.values())
        possible = [x for x in h if h[x] == degree]
        ans = len(nums)
        
        for num in possible:
            for i in range(len(nums)):
                if nums[i] == num:
                    left = i
                    break
            for i in range(len(nums)-1, -1, -1):
                if nums[i] == num:
                    right = i
                    break
            
            if ans > right - left + 1:
                ans = right - left + 1
                
        return ans
        
