class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        ans = []
        for query in queries:
            for word in dictionary:
                changes = 0
                for first, second in zip(query, word):
                    if first != second:
                        changes += 1
                    if changes > 2:
                        break
                        
                if changes <= 2:
                    ans.append(query)
                    break
                    
        return ans
        
