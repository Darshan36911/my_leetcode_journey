from collections import Counter
from math import comb

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        # Build half string counts and middle character
        half = Counter()
        mid = ""

        for ch in sorted(freq):
            half[ch] = freq[ch] // 2
            if freq[ch] % 2:
                mid = ch

        LIMIT = k

        def count_permutations(counter):
            """Return min(number of distinct permutations, LIMIT)."""
            total = sum(counter.values())
            ans = 1

            for cnt in counter.values():
                if cnt == 0:
                    continue
                ans *= comb(total, cnt)
                if ans >= LIMIT:
                    return LIMIT
                total -= cnt

            return ans

        # Not enough palindromes
        if count_permutations(half) < k:
            return ""

        left = []

        total = sum(half.values())

        for _ in range(total):
            for ch in sorted(half.keys()):
                if half[ch] == 0:
                    continue

                half[ch] -= 1

                ways = count_permutations(half)

                if ways >= k:
                    left.append(ch)
                    break
                else:
                    k -= ways
                    half[ch] += 1

        left = "".join(left)
        return left + mid + left[::-1]