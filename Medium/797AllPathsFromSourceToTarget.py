class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
                
        self.ans = []
        self.graph = graph
        self.__find_paths__(0, [0])
        
        return self.ans
        
        
    def __find_paths__(self, cur_index, path):
            
            if cur_index == len(self.graph) - 1:
                self.ans.append(path)
                return
            
            for val in self.graph[cur_index]:
                self.__find_paths__(val, path + [val])
    
