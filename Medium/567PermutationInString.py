class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        needed = Counter(s1)

        for i in range(len(s2)):
            if s2[i] in needed:
                needed[s2[i]] -= 1

            if i >= len(s1) and s2[i - len(s1)] in needed:
                needed[s2[i - len(s1)]] += 1

            if all(frequency == 0 for frequency in needed.values()):
                return True

        return False
