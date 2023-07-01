class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        result = []
        pointer1, pointer2 = 0, 0

        while pointer1 < len(nums1) or pointer2 < len(nums2):
            id1, val1 = nums1[pointer1] if pointer1 < len(nums1) else [float("inf"), 0]
            id2, val2 = nums2[pointer2] if pointer2 < len(nums2) else [float("inf"), 0]

            if id1 == id2:
                result.append([id1, val1 + val2])
                pointer1 += 1
                pointer2 += 1
            elif id1 < id2:
                result.append([id1, val1])
                pointer1 += 1
            else:
                result.append([id2, val2])
                pointer2 += 1

        return result
