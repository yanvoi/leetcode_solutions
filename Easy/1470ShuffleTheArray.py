class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        answer = []
        for x, y in zip(nums[:n], nums[n:]):
            answer.append(x)
            answer.append(y)

        return answer
