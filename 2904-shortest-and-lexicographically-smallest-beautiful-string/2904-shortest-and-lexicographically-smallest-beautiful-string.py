class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = [i for i, ch in enumerate(s) if ch == '1']
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        best = ""
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            length = end - start + 1
            substr = s[start:end+1]
            if length < min_len:
                min_len = length
                best = substr
            elif length == min_len and substr < best:
                best = substr
        
        return best