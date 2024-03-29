class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        wins, losses = set(), dict()
        for winner, loser in matches:
            wins.add(winner)
            losses[loser] = losses.get(loser, 0) + 1
            
        did_not_lose = [player for player in wins if player not in losses]
        lost_one = [player for player in losses if losses[player] == 1]
                
        return [sorted(did_not_lose), sorted(lost_one)]
        
