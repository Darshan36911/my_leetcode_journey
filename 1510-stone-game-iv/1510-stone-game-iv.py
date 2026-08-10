class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        win = [False] * (n + 1)                     # win[i] = current player wins with i stones
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                if not win[i - k * k]:              # move leaves a losing state for opponent
                    win[i] = True
                    break
                k += 1
        return win[n]
        