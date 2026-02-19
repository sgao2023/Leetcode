# Idea

1. Let q = [(x, m, i) for i, (x, m) in enumerate(queries)]
2. Sort q with respect to value of m.
3. Let ans = [-1] * len(q)
4. Sort nums
5. Implement a trie.
6. Two pointers. One pointer iterates q, the other pointer iterates nums: 
    For each (x,m,i) in q, add elements v in nums with value <= m into the trie. 
    Update ans[i] by t.max_xor(x).