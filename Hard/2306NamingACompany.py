class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        # for every letter create a set of suffixes it precedes in ideas
        groups = defaultdict(set)
        for idea in ideas:
            groups[ord(idea[0]) - ord('a')].add(idea[1:])

        # loop over all pairs of letters
        answer = 0
        for group1 in groups.values():
            for group2 in groups.values():
                # get the number of common suffixes since they will not make up new names
                common_count = len(group1 & group2)
                # each suffix can be paired with another suffix from another group (thus the *)
                answer += (len(group1) - common_count) * (len(group2) - common_count)

        return answer
