class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        
        result = []
        greater = False
        
        for i in range(n):
            if greater:
                for c in range(26):
                    if count[c] > 0:
                        result.append(chr(c + ord('a')))
                        count[c] -= 1
                        break
            else:
                found = False
                for c in range(26):
                    if count[c] == 0:
                        continue
                    target_char = ord(target[i]) - ord('a')
                    if c < target_char:
                        continue
                    if c == target_char:
                        count[c] -= 1
                        max_possible = []
                        for cc in range(25, -1, -1):
                            if count[cc] > 0:
                                max_possible.append(chr(cc + ord('a')) * count[cc])
                        max_str = ''.join(max_possible)
                        if max_str > target[i+1:]:
                            result.append(chr(c + ord('a')))
                            found = True
                            break
                        else:
                            count[c] += 1
                            continue
                    else:
                        result.append(chr(c + ord('a')))
                        count[c] -= 1
                        greater = True
                        found = True
                        break
                if not found:
                    return ""
        
        if not greater:
            return ""
        return ''.join(result)