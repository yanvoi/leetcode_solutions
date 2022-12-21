class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_to_t = dict()
        t_to_s = dict()
        for c1, c2 in zip(s, t):
            if (c1 in s_to_t and s_to_t[c1] != c2) or (c2 in t_to_s and t_to_s[c2] != c1):
                return False
            
            s_to_t[c1] = c2
            t_to_s[c2] = c1

        return len(s) == len(t)
