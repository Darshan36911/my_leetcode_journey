class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        if n <= 1: return 0
        prefix = [0] * (n + 1)
        for i in range(n): prefix[i+1] = prefix[i] + stoneValue[i]
        NEG = -(10**18)
        dp = [[0] * n for _ in range(n)]
        suffix_by_r = [None] * n
        for r in range(n):
            suffix_by_r[r] = [NEG] * (r + 2)
            suffix_by_r[r][r] = -prefix[r]
        for l in range(n - 2, -1, -1):
            leftMax = NEG
            m_ptr = l + 1
            for r in range(l + 1, n):
                target = prefix[l] + prefix[r + 1]
                lo, hi = m_ptr, r + 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if 2 * prefix[mid] >= target: hi = mid
                    else: lo = mid + 1
                m_cross = lo
                while m_ptr < m_cross:
                    val = dp[l][m_ptr - 1] + prefix[m_ptr]
                    if val > leftMax: leftMax = val
                    m_ptr += 1
                if m_cross <= r and 2 * prefix[m_cross] == target:
                    val = dp[l][m_cross - 1] + prefix[m_cross]
                    if val > leftMax: leftMax = val
                best_right = suffix_by_r[r][m_cross] + prefix[r + 1]
                dp[l][r] = max(leftMax - prefix[l], best_right)
                suffix_by_r[r][l] = max(dp[l][r] - prefix[l], suffix_by_r[r][l + 1])
        return dp[0][n - 1]