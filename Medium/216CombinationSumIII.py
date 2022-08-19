class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        self.back_track(list(range(1, 10)), k, n, [], ans)
        return ans
        
        
    def back_track(self, array, k, n, path, ans):
            
        if k < 0 or n < 0: return
            
        if k == 0 and n == 0:
            ans.append(path)
            return
            
        for i in range(len(array)):
            self.back_track(array[i+1:], k-1, n - array[i], path + [array[i]], ans)
    
