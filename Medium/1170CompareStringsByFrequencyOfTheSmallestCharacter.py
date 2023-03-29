# first time using bisect.bisect - it's pretty cool
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def f(s):
            return s.count(min(s))

        frequency = sorted([f(word) for word in words])
        return [len(frequency) - bisect.bisect_right(frequency, f(query)) for query in queries]
        
