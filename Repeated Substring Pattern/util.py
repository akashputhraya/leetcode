class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        indices = [i for i, x in enumerate(s) if x == s[0]]
        for i in indices[1:]:
            if len(s)%len(s[:i])==0 and int(len(s)/len(s[:i]))*s[:i]==s:
                    return True
        return False