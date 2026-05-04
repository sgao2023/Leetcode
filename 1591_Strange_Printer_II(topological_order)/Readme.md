# Idea:

Topological sort.

1. Iterate the grid and get the span of every color. This takes O(m*n) time.
2. Get the covering-relationship of the colors. I post two methods here (Solution.py and Solution2.py).
Both take O(m*n*U) time. 

### Method 1
```python
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
```

### Method 2
```python
        for color, (up, dn, le, ri) in span.items():
            for i in range(up, dn + 1):
                for j in range(le, ri + 1):
                    other_color = targetGrid[i][j]
                    if other_color != color and other_color not in g[color]:
                        g[color].add(other_color)
                        in_deg[other_color] += 1
```

The second one is better, and turns out to be faster than the first.
Iterating over a list is faster than iterating over a dictionary.

The first method iterates the dictionary too often.