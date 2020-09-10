class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word_endings = [j for j, ch in enumerate(str) if ch == ' ']
        word_endings.append(len(str))
        pattern_dict = {}
        translated_str = ''
        if len(pattern)!=str.count(' ')+1:
            return False
        start = 0
        for i in range(len(pattern)):
            end = word_endings[i] + 1
            current_str = str[start:end].strip()
            if pattern[i] not in pattern_dict.values() and current_str not in pattern_dict:
                pattern_dict[current_str] = pattern[i]
            translated_str+=(pattern_dict.get(current_str) if pattern_dict.get(current_str) else '')
            if pattern[:i+1]!=translated_str[:i+1]:
                return False
            start = end
        return True