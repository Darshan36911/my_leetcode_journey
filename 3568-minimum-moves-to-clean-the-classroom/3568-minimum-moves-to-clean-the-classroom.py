from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])
        
        start = None
        litter = []
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))
        
        k = len(litter)
        if k == 0:
            return 0
        
        litter_idx = {pos: i for i, pos in enumerate(litter)}
        all_mask = (1 << k) - 1
        
        max_energy_for = {}
        queue = deque()
        
        key = (start[0], start[1], 0)
        max_energy_for[key] = energy
        queue.append((start[0], start[1], 0, energy, 0))
        
        while queue:
            r, c, mask, e, moves = queue.popleft()
            
            if mask == all_mask:
                return moves
            
            if e <= 0:
                continue
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    new_e = e - 1
                    if classroom[nr][nc] == 'R':
                        new_e = energy
                    
                    new_mask = mask
                    if classroom[nr][nc] == 'L' and (nr, nc) in litter_idx:
                        new_mask |= (1 << litter_idx[(nr, nc)])
                    
                    key = (nr, nc, new_mask)
                    if key not in max_energy_for or new_e > max_energy_for[key]:
                        max_energy_for[key] = new_e
                        queue.append((nr, nc, new_mask, new_e, moves + 1))
        
        return -1