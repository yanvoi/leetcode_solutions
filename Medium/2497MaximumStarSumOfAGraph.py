class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        
        neighbors = [[] for _ in range(len(vals))]
        for first, second in edges:
            neighbors[first].append(second)
            neighbors[second].append(first)
            
        value = dict()
        for i, v in enumerate(vals):
            value[i] = v
            
        ans = float('-inf')
        for i, val in enumerate(vals):
            cur_sum = val
            
            adjacent = sorted([value[k] for k in neighbors[i]], reverse=True)
            for adj in adjacent[:k]:
                if adj > 0:
                    cur_sum += adj
                
            ans = max(ans, cur_sum)
            
        return ans
        
