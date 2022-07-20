class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        for i in range(0, len(nums), 2):
            to_pop = nums.pop(i + n)
            nums.insert(i + 1, to_pop)
            n = n - 1

        return nums
    
