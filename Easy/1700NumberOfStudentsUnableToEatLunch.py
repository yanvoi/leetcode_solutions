# only students queue moves
# O(n) time, O(1) space (needed_sandwiches will always have at most 2 keys)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        needed_sandwiches = Counter(students)
        i, j = 0, len(students)
        while i < j and needed_sandwiches[sandwiches[i]]:
            needed_sandwiches[sandwiches[i]] -= 1
            i += 1

        return j - i
