class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(student - seat) for student, seat in zip(sorted(students), sorted(seats)))
        
