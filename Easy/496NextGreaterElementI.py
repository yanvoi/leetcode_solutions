class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        h = dict()
        for i in range(len(nums2)):
            h[nums2[i]] = i
            
        ans = []
        for i in range(len(nums1)):
            index = h[nums1[i]]
            found = -1
            for j in range(index + 1, len(nums2)):
                if nums1[i] < nums2[j]:
                    found = nums2[j]
                    break
            ans.append(found)
            
        return ans
