# brute force solution - we're checking all possible sequences
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        self.unique = set()
        self._dfs("", tiles)
        # - 1 because an empty sequence doesn't count
        return len(self.unique) - 1

    
    def _dfs(self, sequence, tiles):
        if sequence in self.unique:
            return

        self.unique.add(sequence)

        for i in range(len(tiles)):
            # after adding a letter to the sequence remove it from tiles
            self._dfs(sequence + tiles[i], tiles[:i] + tiles[i+1:])
        
