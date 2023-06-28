class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        answer = 0
        seen_nums = set()
        for num in nums:
            if (num - diff) in seen_nums and (num - 2 * diff) in seen_nums:
                answer += 1
            seen_nums.add(num)

        return answer
