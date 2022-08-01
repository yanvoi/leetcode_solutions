class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        placements = sorted(score, reverse=True)
        h = dict()
        for i in range(len(placements)):
            h[placements[i]] = i
            
        answer = []
        for athlete in score:
            if h[athlete] == 0:
                answer.append('Gold Medal')
            elif h[athlete] == 1:
                answer.append('Silver Medal')
            elif h[athlete] == 2:
                answer.append('Bronze Medal')
            else:
                answer.append(str(h[athlete] + 1))
            
        return answer
            
