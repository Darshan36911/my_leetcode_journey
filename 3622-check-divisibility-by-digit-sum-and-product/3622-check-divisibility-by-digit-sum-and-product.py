class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        digit_sum = sum(digits)
        digit_product = 1
        for d in digits:
            digit_product *= d
        return n % (digit_sum + digit_product) == 0