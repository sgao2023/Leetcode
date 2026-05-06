# Idea:

Union Find + Topological Sort

Based on the matrix, we build a directed graph. We assign the rank of the elements based on their topological order.

1. Why Union Find:

Without Union Find: If a row is given as [1, 1, ..., 1, 2, 2, ..., 2], in which there are 100 ones and 100 twos, then we add an edge from every 1 to every 2. There would be too many edges, which leads to a high complexity.

With Union Find, we can reduce the above edges to a single edge.

2. Some issues with my initial solution (although it's accepted):
    1. The way of implementation of the graph: I use list to store the neighbors, which may cause multiple edges and multiple calculation of in-degree. In the final version I use set, instead of list, to store the neighbors.
    2. Update of rank is changed from ```python rank[y] = rank[x] + 1``` to ```python rank[y] = max(rank.get(y, 1), rank[x] + 1)```. I believe the original version works, but it needs a bit mathematical proof. (The ranks of the dequeued elements are monotonically increasing, so smaller rank wouldn't cover greater rank.) The new version is explicit and easier to understand. 