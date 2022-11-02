class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        ans = 0
        positions = dict()
        for i, num in enumerate(nums):
            positions[num] = positions.get(num, []) + [i]
            
        for arr in positions.values():
            for i in range(len(arr) - 1):
                for j in range(i+1, len(arr)):
                    if (arr[i] * arr[j]) % k == 0:
                        ans += 1
                        
        return ans
        
