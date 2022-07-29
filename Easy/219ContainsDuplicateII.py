class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = dict()
        
        for index, val in enumerate(nums):
            if val in visited and abs(visited[val] - index) <= k:
                return True
            
            visited[val] = index
        
        return False
        
