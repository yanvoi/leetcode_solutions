class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:

        clips.sort(key = lambda x: (x[0], -x[1]))
        answer = 0
        last_finished, the_latest_end = -1, 0

        for start, finish in clips:
            if the_latest_end >= time or start > the_latest_end:
                break
            if last_finished < start:
                answer += 1
                last_finished = the_latest_end
            the_latest_end = max(the_latest_end, finish)

        return answer if the_latest_end >= time else -1
