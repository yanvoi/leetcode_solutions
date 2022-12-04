class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        
        # if k == 1 we're looking for the 'smallest' permutation lexicographically
        if k == 1:
            return min(s[i:] + s[:i] for i in range(len(s)))
        
        # if k > 1 we can turn the string to whatever we want, so we might as well sort it
        return ''.join(sorted(s))
        
