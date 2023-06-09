class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        s_pointer, t_pointer = 0, 0
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                t_pointer += 1
            s_pointer += 1

        return len(t) - t_pointer
