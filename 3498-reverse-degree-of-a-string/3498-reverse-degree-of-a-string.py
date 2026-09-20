class Solution:
    def reverseDegree(self, s):
        total = 0
        for i, c in enumerate(s, 1):
            total += i * (ord('z') - ord(c) + 1)
        return total