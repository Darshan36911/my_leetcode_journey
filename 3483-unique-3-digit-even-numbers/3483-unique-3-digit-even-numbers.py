from itertools import permutations


class Solution:
    def totalNumbers(self, digits):
        seen = set()
        for p in permutations(digits, 3):
            if p[0] == 0:
                continue
            if p[2] % 2 != 0:
                continue
            seen.add(p)
        return len(seen)