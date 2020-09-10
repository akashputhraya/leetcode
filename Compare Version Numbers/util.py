class Solution:
    def remove_trailing_zeroes(self, v: str) -> str:
        while len(v) > 1 and v[-1] == 0:
            del v[-1]
        return v

    def compareVersion(self, version1: str, version2: str) -> int:
        version1_split = self.remove_trailing_zeroes(list(map(int, version1.split('.'))))
        version2_split = self.remove_trailing_zeroes(list(map(int, version2.split('.'))))
        if len(version1_split) <= len(version2_split):
            shorter = 1
            shorter_version = version1_split
            longer_version = version2_split
        else:
            shorter = 2
            shorter_version = version2_split
            longer_version = version1_split
        for i in range(len(shorter_version)):
            if shorter_version[i] < longer_version[i]:
                return -1 if shorter == 1 else 1
            elif shorter_version[i] > longer_version[i]:
                return -1 if shorter == 2 else 1
            else:
                continue

        if len(longer_version) > i + 1:
            return -1 if shorter == 1 else 1
        else:
            return 0
