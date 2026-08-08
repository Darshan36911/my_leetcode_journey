class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        # suffix[i] = longest suffix of word2 matchable as subsequence of word1[i:]
        suffix = [0] * (n + 1)
        p = m - 1
        for i in range(n - 1, -1, -1):
            if p >= 0 and word1[i] == word2[p]:
                p -= 1
            suffix[i] = m - 1 - p

        ans = []
        mismatch_used = False
        i = 0
        for j in range(m):
            while i < n:
                if word1[i] == word2[j]:
                    break                       # perfect match
                if not mismatch_used and suffix[i + 1] >= m - j - 1:
                    break                       # use the one mismatch here
                i += 1                          # unusable index, skip
            if i == n:
                return []                       # can't complete
            if word1[i] != word2[j]:
                mismatch_used = True
            ans.append(i)
            i += 1
        return ans