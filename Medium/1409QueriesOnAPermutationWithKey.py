class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        result = []
        permutation = [i+1 for i in range(m)]
        for query in queries:
            index = permutation.index(query)
            result.append(index)
            permutation.pop(index)
            permutation.insert(0, query)

        return result
        
