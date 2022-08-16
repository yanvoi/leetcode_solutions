class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        self.back_track(candidates, target, [], ans)
        return ans
        
    def back_track(self, array, target_num, path, answer):
        
        if target_num < 0: return
        
        if target_num == 0:
            answer.append(path)
            return
        
        for i in range(len(array)):
            self.back_track(array[i:], target_num - array[i], path + [array[i]], answer)
        
