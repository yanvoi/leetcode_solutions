class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if not nums: return
        pivot = random.choice(nums)
        
        greater = [num for num in nums if num > pivot]
        equal = [num for num in nums if num == pivot]
        lesser = [num for num in nums if num < pivot]
        
        greaterLen = len(greater)
        equalLen = len(equal)
        
        if k <= greaterLen:
            return self.findKthLargest(greater, k)
        elif k > greaterLen + equalLen:
            return self.findKthLargest(lesser, k - greaterLen - equalLen)
        else:
            return equal[0]
        
