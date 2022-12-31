class Solution:
    def hIndex(self, citations: List[int]) -> int:

        left, right = 0, len(citations) - 1
        citations_num = len(citations)

        while left <= right:
            mid = (left + right) // 2

            if citations[mid] >= citations_num - mid:
                right = mid - 1
            else:
                left = mid + 1

        return citations_num - left
