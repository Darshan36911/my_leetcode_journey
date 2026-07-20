class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def backtrack(path):
            if len(path) == n:
                ans.append("".join(path))
                return

            for ch in "abc":
                if not path or path[-1] != ch:
                    path.append(ch)
                    backtrack(path)
                    path.pop()

        backtrack([])

        if k > len(ans):
            return ""

        return ans[k - 1]