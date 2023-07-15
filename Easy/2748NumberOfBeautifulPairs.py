class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:

        answer = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num1, num2 = int(str(nums[i])[0]), int(str(nums[j])[-1])
                answer += gcd(num1, num2) == 1

        return answer
