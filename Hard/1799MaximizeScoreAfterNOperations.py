# first time using the bitmask approach and it's brilliant for this type of problems
class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @cache
        def dfs(pair, mask):
            if pair > len(nums) // 2:
                return 0

            cur_answer = 0
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    new_mask = (1 << i) + (1 << j)
                    if not (mask & new_mask):
                        gcd = math.gcd(nums[i], nums[j])
                        cur_answer = max(cur_answer, pair * gcd + dfs(pair + 1, mask + new_mask))

            return cur_answer
        
        return dfs(1, 0)
