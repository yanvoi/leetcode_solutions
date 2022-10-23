class Solution:

    def __init__(self, nums: List[int]):
        self.shuffled = nums
        self.original = nums.copy()
        

    def reset(self) -> List[int]:
        self.shuffled = self.original.copy()
        return self.shuffled
        

    def shuffle(self) -> List[int]:
        
        for i in range(len(self.shuffled)):
            rand = random.randrange(i, len(self.shuffled))
            self.shuffled[i], self.shuffled[rand] = self.shuffled[rand], self.shuffled[i]
            
        return self.shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
