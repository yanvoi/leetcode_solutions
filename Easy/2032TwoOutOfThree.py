class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        first = set(nums1)
        second = set(nums2)
        third = set(nums3)
        
        return list((first & second) | (first & third) | (second & third))
        
