class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # DP for length = 2
        up = [0] * m
        down = [0] * m

        for v in range(m):
            up[v] = v            # choose previous value < v
            down[v] = m - 1 - v # choose previous value > v

        # Build lengths 3..n
        for _ in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            # prefix sums of down
            pref = [0] * (m + 1)
            for i in range(m):
                pref[i + 1] = (pref[i] + down[i]) % MOD

            # suffix sums of up
            suff = [0] * (m + 1)
            for i in range(m - 1, -1, -1):
                suff[i] = (suff[i + 1] + up[i]) % MOD

            for v in range(m):
                # last move becomes up: previous value must be smaller
                new_up[v] = pref[v]

                # last move becomes down: previous value must be larger
                new_down[v] = suff[v + 1]

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD