class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        processed = []
        groups = []
        current_max = 0
        for i in range(len(S)):
            if S[i] not in processed:
                letter_max = len(S)-S[::-1].find(S[i])-1
                if i > current_max:
                    groups.append(current_max+1-sum(groups))
                if letter_max==len(S)-1:
                    groups.append(letter_max+1-sum(groups))
                    break
                if letter_max > current_max:
                    current_max = letter_max
                processed.append([S[i]])
            else:
                continue
        return groups