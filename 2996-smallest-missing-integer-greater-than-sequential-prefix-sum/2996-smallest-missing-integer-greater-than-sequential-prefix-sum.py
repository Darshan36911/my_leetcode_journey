class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1

        present = set(nums)
        x = s
        while x in present:
            x += 1
        return x