class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        def deserialize(arr):
            
            if self.index >= len(arr):
                self.index += 1
                return
            
            val = arr[self.index]
            self.index += 1
            
            if val != '#':
                deserialize(arr)
                deserialize(arr)
                
        
        self.index = 0
        p = preorder.split(',')
        deserialize(p)
        
        return self.index == len(p)
        
