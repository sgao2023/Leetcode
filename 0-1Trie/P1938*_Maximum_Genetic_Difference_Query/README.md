# Idea
1. Extract the info of queries into a dictionary d, where key-value pair of d has the form
```
node -> [(val1, q_id1), (val2, q_id2), ...] 
```
Let ans = [0] * len(queries). 
2. Write a dfs function to traverse the tree. In each step, keep the path from root to curr_node. (At the very beginning, insert curr_node_val into trie, remove curr_node_val at the end of the function.) If curr_node is in queries, update the ans array. 

Core logic:
```
        t = Trie()
        def dfs(node):
            t.insert(node)
            if node in d:
                for pair in d[node]:
                    val, q_id = pair
                    ans[q_id] = t.max_xor(val)
            for son in g[node]:
                dfs(son)
            t.remove(node)
        
        dfs(root)
```