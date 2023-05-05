class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        radiant = set(i for i in range(len(senate)) if senate[i] == "R")
        dire = set(i for i in range(len(senate)) if senate[i] == "D")

        i = 0
        while radiant and dire:
            cur = i % len(senate)
            i += 1
            if cur not in radiant and cur not in dire:
                continue
            
            to_ban = (cur + 1) % len(senate)
            while (to_ban not in radiant and to_ban not in dire) or senate[to_ban] == senate[cur]:
                to_ban = (to_ban + 1) % len(senate)

            if to_ban in dire:
                dire.remove(to_ban)
            else:
                radiant.remove(to_ban)

        return "Radiant" if radiant else "Dire"
