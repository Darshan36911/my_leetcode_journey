class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((nums[i], i) for i in range(n))

        values = [0] * n
        pos = [0] * n

        for i, (val, idx) in enumerate(arr):
            values[i] = val
            pos[idx] = i

        # far[i] = farthest sorted index reachable in one edge
        far = [0] * n
        r = 0
        for i in range(n):
            while r + 1 < n and values[r + 1] - values[i] <= maxDiff:
                r += 1
            far[i] = r

        LOG = n.bit_length()
        up = [far[:]]

        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            a, b = pos[u], pos[v]
            if a > b:
                a, b = b, a

            if a == b:
                ans.append(0)
                continue

            cur = a
            steps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    steps += 1 << k

            if far[cur] < b:
                ans.append(-1)
            else:
                ans.append(steps + 1)

        return ans