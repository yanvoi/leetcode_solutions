class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if not nums: return
        pivot = random.choice(nums)
        
        greater, equal, lesser = [], [], []
        
        for num in nums:
            if num > pivot: greater.append(num)
            elif num == pivot: equal.append(num)
            else: lesser.append(num)
        
        greaterLen = len(greater)
        equalLen = len(equal)
        
        if k <= greaterLen:
            return self.findKthLargest(greater, k)
        elif k > greaterLen + equalLen:
            return self.findKthLargest(lesser, k - greaterLen - equalLen)
        else:
            return equal[0]
        
