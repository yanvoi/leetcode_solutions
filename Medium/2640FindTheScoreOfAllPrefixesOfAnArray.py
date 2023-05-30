class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:

        max_num = float('-inf')
        answer = [0] * len(nums)
        for i, num in enumerate(nums):
            max_num = max(max_num, num)
            answer[i] += max_num + num + answer[i-1] if i else max_num + num

        return answer
