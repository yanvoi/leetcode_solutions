class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        bulls, cows, secret_off, guess_off = 0, 0, defaultdict(int), defaultdict(int)
        for i, (s, g) in enumerate(zip(secret, guess)):
            if s == g:
                bulls += 1
            else:
                secret_off[s] += 1
                guess_off[g] += 1

            if secret_off[g] and guess_off[g]:
                secret_off[g] -= 1
                guess_off[g] -= 1
                cows += 1

            if secret_off[s] and guess_off[s]:
                secret_off[s] -= 1
                guess_off[s] -= 1
                cows += 1

        return f'{str(bulls)}A{str(cows)}B'
