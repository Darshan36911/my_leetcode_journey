class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)
        indexed = sorted((nums[i], i) for i in range(n))
        
        groups = []
        for i in range(n):
            if i == 0 or indexed[i][0] - indexed[i-1][0] > limit:
                groups.append([indexed[i]])
            else:
                groups[-1].append(indexed[i])
        
        for group in groups:
            vals = sorted([v for v, idx in group])
            pos = sorted([idx for v, idx in group])
            for v, p in zip(vals, pos):
                nums[p] = v
        
        return nums