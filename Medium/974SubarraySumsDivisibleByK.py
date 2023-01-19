class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        answer, prefix = 0, 0
        modCount = [1] + [0] * k

        for num in nums:
            prefix = (prefix + num) % k
            answer += modCount[prefix]
            modCount[prefix] += 1

        return answer
