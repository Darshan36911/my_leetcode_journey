from bisect import bisect_right, insort


class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        items = sorted((r, l, w, idx) for idx, (l, r, w) in enumerate(intervals))
        ends = [it[0] for it in items]
        starts = [it[1] for it in items]
        weights = [it[2] for it in items]
        origs = [it[3] for it in items]

        P = [bisect_right(ends, starts[i] - 1) - 1 for i in range(n)]

        pref = [[None] * n for _ in range(4)]

        for c in range(1, 5):
            cur = [None] * n
            best = None
            for i in range(n):
                if P[i] < 0:
                    ext_weight = weights[i]
                    ext_tuple = (origs[i],)
                elif c == 1:
                    ext_weight = weights[i]
                    ext_tuple = (origs[i],)
                else:
                    pv = pref[c - 2][P[i]]
                    ext_weight = pv[0] + weights[i]
                    tmp = list(pv[1])
                    insort(tmp, origs[i])
                    ext_tuple = tuple(tmp)
                cur[i] = (ext_weight, ext_tuple)
                if best is None or cur[i][0] > best[0] or (
                        cur[i][0] == best[0] and cur[i][1] < best[1]):
                    best = cur[i]
                pref[c - 1][i] = best

        return list(pref[3][n - 1][1])