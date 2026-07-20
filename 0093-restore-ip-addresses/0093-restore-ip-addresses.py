class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    ans.append(".".join(path))
                return

            for end in range(start, min(start + 3, len(s))):
                part = s[start:end + 1]

                # Leading zero check
                if len(part) > 1 and part[0] == '0':
                    break

                # Value check
                if int(part) <= 255:
                    path.append(part)
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return ans