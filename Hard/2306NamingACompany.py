class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        # for every letter in the alphabet create a set of suffixes it precedes in ideas
        groups = [set() for _ in range(26)]
        for idea in ideas:
            groups[ord(idea[0]) - ord('a')].add(idea[1:])

        # loop over all pairs of letters
        answer = 0
        for i in range(26):
            for j in range(26):
                # get the number of common suffixes since they will not make up new names
                common_count = len(groups[i] & groups[j])
                # each suffix can be paired with another suffix from another group (thus the *)
                answer += (len(groups[i]) - common_count) * (len(groups[j]) - common_count)

        return answer
