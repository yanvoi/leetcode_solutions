class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r_stack = [i for i in range(len(senate)) if senate[i] == "R"]
        d_stack = [i for i in range(len(senate)) if senate[i] == "D"]

        banned = set()
        i = 0
        while r_stack and d_stack:
            cur = i % len(senate)
            if cur not in banned:
                helper = (cur + 1) % len(senate)
                while helper in banned or senate[helper] == senate[cur]:
                    helper = (helper + 1) % len(senate)

                banned.add(helper)
                if senate[cur] == "R":
                    d_stack.pop(d_stack.index(helper))
                else:
                    r_stack.pop(r_stack.index(helper))

            i += 1

        return "Radiant" if r_stack else "Dire"
