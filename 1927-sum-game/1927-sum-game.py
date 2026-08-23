class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0
        
        for i, ch in enumerate(num):
            if i < half:
                if ch == '?':
                    left_q += 1
                else:
                    left_sum += int(ch)
            else:
                if ch == '?':
                    right_q += 1
                else:
                    right_sum += int(ch)
        
        diff = left_sum - right_sum
        q_diff = right_q - left_q
        
        if q_diff % 2 == 1:
            return True
        
        return diff != 9 * q_diff // 2