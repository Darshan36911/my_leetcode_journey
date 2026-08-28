class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        odd_count = sum(1 for c in count if c % 2 == 1)
        if (n % 2 == 0 and odd_count > 0) or (n % 2 == 1 and odd_count != 1):
            return ""
        
        m = (n + 1) // 2
        target_ord = [ord(ch) - ord('a') for ch in target]
        
        def build_max_pal(partial, counts):
            rem = counts[:]
            suffix = []
            for j in range(len(partial), m):
                if j == m - 1 and n % 2 == 1:
                    for c in range(25, -1, -1):
                        if rem[c] >= 1:
                            suffix.append(chr(c + ord('a')))
                            rem[c] -= 1
                            break
                else:
                    for c in range(25, -1, -1):
                        if rem[c] >= 2:
                            suffix.append(chr(c + ord('a')))
                            rem[c] -= 2
                            break
            H = partial + ''.join(suffix)
            if n % 2 == 0:
                return H + H[::-1]
            else:
                return H + H[-2::-1]
        
        def build_min_suffix(counts, from_pos):
            rem = counts[:]
            suffix = []
            for j in range(from_pos, m):
                if j == m - 1 and n % 2 == 1:
                    for c in range(26):
                        if rem[c] >= 1:
                            suffix.append(chr(c + ord('a')))
                            rem[c] -= 1
                            break
                else:
                    for c in range(26):
                        if rem[c] >= 2:
                            suffix.append(chr(c + ord('a')))
                            rem[c] -= 2
                            break
            return ''.join(suffix)
        
        def dfs(i, state, counts, partial):
            if i == m:
                if state == 1:
                    return ""
                if n % 2 == 0:
                    P = partial + partial[::-1]
                else:
                    P = partial + partial[-2::-1]
                return "" if P > target else None
            
            is_mid = (i == n - 1 - i)
            
            if state == 1:
                return build_min_suffix(counts, i)
            
            for c in range(26):
                need = 1 if is_mid else 2
                if counts[c] < need:
                    continue
                if c < target_ord[i]:
                    continue
                
                new_state = 1 if c > target_ord[i] else 0
                counts[c] -= need
                
                feasible = True
                if new_state == 0:
                    P_max = build_max_pal(partial + chr(c + ord('a')), counts)
                    feasible = P_max > target
                
                if feasible:
                    res = dfs(i + 1, new_state, counts, partial + chr(c + ord('a')))
                    if res is not None:
                        counts[c] += need
                        return chr(c + ord('a')) + res
                
                counts[c] += need
            return None
        
        H = dfs(0, 0, count[:], "")
        if H is None:
            return ""
        if n % 2 == 0:
            return H + H[::-1]
        else:
            return H + H[-2::-1]