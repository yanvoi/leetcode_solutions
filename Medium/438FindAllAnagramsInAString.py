class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        needed = Counter(p)
        answer = []
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] in needed:
                needed[s[i]] -= 1

            if i + len(p) < len(s) and s[i + len(p)] in needed:
                needed[s[i + len(p)]] += 1

            if all(count == 0 for count in needed.values()):
                answer.append(i)

        return answer[::-1]
