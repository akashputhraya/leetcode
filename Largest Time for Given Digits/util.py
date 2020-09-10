class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        counts = {}
        pairs = []
        hrs = []
        r = ""

        for i in range(len(A)):
            if A[i] in counts:
                counts[A[i]] += 1
            else:
                counts[A[i]] = 1
            for j in range(len(A)):
                if i != j:
                    pairs.append(A[i] * 10 + A[j])
        pairs = sorted(list(set(pairs)), reverse=True)

        pairs = [x for x in pairs if x <= 59]

        for p in pairs:
            if p <= 23:
                hrs.append(p)

        for h in hrs:
            for p in pairs:
                hrs_count = {}
                tm = (str(h) if h >= 10 else '0' + str(h)) + (str(p) if p >= 10 else '0' + str(p))
                for i in range(len(tm)):
                    if int(tm[i]) in hrs_count:
                        hrs_count[int(tm[i])] += 1
                        if hrs_count[int(tm[i])] > counts[int(tm[i])]:
                            break
                        else:
                            r = (str(h) if h >= 10 else '0' + str(h)) + ':' + (str(p) if p >= 10 else '0' + str(p))
                            if i == len(tm) - 1:
                                return r
                    else:
                        hrs_count[int(tm[i])] = 1
                        if i == len(tm) - 1:
                            r = (str(h) if h >= 10 else '0' + str(h)) + ':' + (str(p) if p >= 10 else '0' + str(p))
                            return r
        return ""