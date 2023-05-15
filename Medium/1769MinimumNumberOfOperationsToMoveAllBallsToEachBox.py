class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        answer = [0] * len(boxes)

        balls_so_far = 0
        moves = 0
        for i in range(len(boxes)):
            answer[i] += moves
            balls_so_far += boxes[i] == "1"
            moves += balls_so_far

        balls_so_far = 0
        moves = 0
        for i in range(len(boxes) - 1, -1, -1):
            answer[i] += moves
            balls_so_far += boxes[i] == "1"
            moves += balls_so_far

        return answer
