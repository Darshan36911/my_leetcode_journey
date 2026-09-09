class Solution:
    def countCommas(self, n):
        count = 0
        commas = 1
        start = 1000
        end = 999999
        while start <= n:
            count += commas * (min(n, end) - start + 1)
            commas += 1
            start *= 1000
            end = end * 1000 + 999
        return count