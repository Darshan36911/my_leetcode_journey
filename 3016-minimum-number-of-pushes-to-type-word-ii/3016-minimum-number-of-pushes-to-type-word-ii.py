from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        frequencies = sorted(freq.values(), reverse=True)

        ans = 0

        for i, f in enumerate(frequencies):
            pushes = i // 8 + 1
            ans += f * pushes

        return ans