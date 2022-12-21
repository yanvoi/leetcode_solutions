class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        answer = [0] * len(deck)
        next_index = collections.deque(range(len(deck)))

        for card in sorted(deck):
            answer[next_index.popleft()] = card
            # for every card we reveal, we place the next one at the end
            if next_index:
                next_index.append(next_index.popleft())

        return answer
