class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        start, dest = set(), set()
        
        for path in paths:
            start.add(path[0])
            dest.add(path[1])
            
        return dest.difference(start).pop()
        
