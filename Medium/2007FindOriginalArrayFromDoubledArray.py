class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        counter = collections.Counter(changed)
        ans = []
        
        for key in counter.keys():
            
            if key == 0:
                if counter[key] % 2 == 1:
                    return []
                else:
                    ans += [0] * (counter[key] // 2)
                    
            elif counter[key] > 0:
                
                k = key
                
                while k % 2 == 0 and k // 2 in counter:
                    k = k // 2
                    
                while k in counter:
                    if counter[k] > 0:
                        if counter[k+k] < counter[k]:
                            return []
                        
                        ans += [k] * counter[k]
                        counter[k+k] = counter[k+k] - counter[k]
                        counter[k] = 0
                        
                    k += k
                        
        return ans
        
