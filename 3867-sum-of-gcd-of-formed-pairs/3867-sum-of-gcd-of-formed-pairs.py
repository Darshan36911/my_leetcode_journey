from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []

        max_so_far = 0
        for num in nums:
            max_so_far = max(max_so_far, num)
            prefixGcd.append(gcd(max_so_far, num))

        prefixGcd.sort()

        ans = 0
        left, right = 0, len(prefixGcd) - 1

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans