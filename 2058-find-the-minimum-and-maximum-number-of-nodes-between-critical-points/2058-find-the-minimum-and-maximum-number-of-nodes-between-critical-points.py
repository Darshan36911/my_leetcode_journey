class Solution:
    def nodesBetweenCriticalPoints(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        criticals = []
        for i in range(1, len(vals) - 1):
            if (vals[i] > vals[i-1] and vals[i] > vals[i+1]) or \
               (vals[i] < vals[i-1] and vals[i] < vals[i+1]):
                criticals.append(i)
        
        if len(criticals) < 2:
            return [-1, -1]
        
        min_dist = min(criticals[i+1] - criticals[i] for i in range(len(criticals)-1))
        max_dist = criticals[-1] - criticals[0]
        return [min_dist, max_dist]