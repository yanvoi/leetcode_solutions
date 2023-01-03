class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        answer = []
        groups = dict()

        for person, group_size in enumerate(groupSizes):
            # we add each person to a group consisting of groupSizes[person] people
            groups[group_size] = groups.get(group_size, []) + [person]

            # when we find enough people for a group, we add this group to the answer list
            # and empty the dict[group_size] so we can have more groups of given size
            if len(groups[group_size]) == group_size:
                answer.append(groups[group_size])
                del groups[group_size]

        return answer
        
