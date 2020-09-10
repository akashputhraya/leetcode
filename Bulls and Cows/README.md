`**Example input**:
 secret = "1807", guess = "7810"`

 **Approach:**
 1. bulls = 0, cows = 0
 2. For every unique digit in secret that is also in guess, add an entry in the following two dictionaries:
    * secret_positions: {digit : sorted list of indexes in secret where the digit occurs}
    * guess_positions: {digit : sorted list of indexes in guess where the digit occurs}
 3. After addition to the dictionary, check for the number of common positions for that letter in secret_positions and guess_positions (say x)
 4. bulls = bulls+x
 5. If the remaining number of positions for that letter in secret (remaining_secret) <= remaining number of postions for that letter in guess (remaining_guess), then: cows = cows + (remaining_secret - x)
 6. Otherwise: cows = cows + (remaining_guess - x)