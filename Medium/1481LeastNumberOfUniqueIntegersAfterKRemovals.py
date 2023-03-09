class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        stack = sorted([count for count in Counter(arr).values()], reverse=True)
        
        while stack and k - stack[-1] >= 0:
            k -= stack.pop()

        return len(stack)
