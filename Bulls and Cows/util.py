import re

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_positions = {}
        guess_positions = {}
        processed = []
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i] not in processed:
                i_in_guess = sorted([ch.start() for ch in re.finditer(secret[i], guess)])
                if i_in_guess:
                    i_in_secret = sorted([ch.start() for ch in re.finditer(secret[i], secret)])
                    secret_positions[secret[i]] = i_in_secret
                    guess_positions[secret[i]] = i_in_guess
                    if i_in_secret == i_in_guess:
                        bulls += len(i_in_secret)
                    else:
                        bulls_at_i = len(set(i_in_secret).intersection(i_in_guess))
                        bulls += bulls_at_i
                        if len(i_in_secret) - bulls_at_i <= len(i_in_guess) - bulls_at_i:
                            cows += (len(i_in_secret) - bulls_at_i)
                        else:
                            cows += (len(i_in_guess) - bulls_at_i)
            processed.append(secret[i])

        return str(bulls) + "A" + str(cows) + "B"