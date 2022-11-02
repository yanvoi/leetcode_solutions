class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        indices = dict()
        for name, height in zip(names, heights):
            indices[height] = name
            
        heights.sort(reverse=True)
        return [indices[h] for h in heights]
        
