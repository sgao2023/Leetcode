from typing import List
from collections import defaultdict
from collections import deque
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
        m = len(targetGrid)
        n = len(targetGrid[0])

        # Get the span of each color.
        span = dict()
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                if c not in span:
                    span[c] = [i, i, j, j]
                else:
                    span[c][0] = min(span[c][0], i)
                    span[c][1] = max(span[c][1], i)
                    span[c][2] = min(span[c][2], j)
                    span[c][3] = max(span[c][3], j)
        
        # Construct the graph, and calculate in-degrees. 
        g = defaultdict(set)
        in_deg = {x:0 for x in span.keys()}
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                for k, ls in span.items():
                    if k == c: 
                        continue
                    up, dn, le, ri = ls
                    if up <= i <= dn and le <= j <= ri:
                        if c not in g[k]:
                            g[k].add(c)
                            in_deg[c] += 1
        
        # Topological sort.
        # Store the printable colors in the set can_print.
        q = deque()
        for i, deg in in_deg.items():
            if deg == 0:
                q.append(i)
        
        can_print = set()
        while q:
            x = q.popleft()
            can_print.add(x)
            for y in g[x]:
                in_deg[y] -= 1
                if in_deg[y] == 0:
                    q.append(y)

        # Return if all colors can be printed.
        return len(can_print) == len(span)