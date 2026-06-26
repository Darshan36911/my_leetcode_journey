from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        offset = n + 2
        size = 2 * n + 5

        bit = [0] * size

        def update(i):
            while i < size:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        pref = 0
        ans = 0

        # Initial prefix sum = 0
        update(offset)

        for x in nums:
            pref += 1 if x == target else -1
            idx = pref + offset
            ans += query(idx - 1)   # previous prefix sums < current
            update(idx)

        return ans