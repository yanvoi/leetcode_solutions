class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_for_leet = dict()
        
        for i in range(len(nums)):
            if nums[i] in hash_for_leet:
                hash_for_leet[nums[i]] += 1
            else:
                hash_for_leet[nums[i]] = 1
        
        for element in hash_for_leet:
            if hash_for_leet[element] > len(nums) / 2:
                return element
        return None
