class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        n1 = set(nums1)
        n2 = set(nums2)

        return [list(n1.difference(n2)), list(n2.difference(n1))]
