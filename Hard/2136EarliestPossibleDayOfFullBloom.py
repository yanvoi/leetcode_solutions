class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        cur_plant_time = 0
        ans = 0
        
        # the whole idea is that we first plant seeds that take the longest to grow
        indices = sorted(range(len(growTime)), key=lambda x: growTime[x], reverse=True)
        
        for i in indices:
            cur_plant_time += plantTime[i]
            # flowers can grow while we plant other seeds
            ans = max(ans, cur_plant_time + growTime[i])
            
        return ans
        
