class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]
        
        best = prefix[n]
        for i in range(n - 2, 0, -1):
            best = max(best, prefix[i + 1] - best)
        return best