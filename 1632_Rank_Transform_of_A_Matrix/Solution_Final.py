# 模板来源 https://leetcode.cn/circle/discuss/mOr1u6/
class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己，大小为 1
        self._fa = list(range(n))  # 代表元
        self._size = [1] * n  # 集合大小
        self.cc = n  # 连通块个数
        

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        fa = self._fa
        # 如果 fa[x] == x，则表示 x 是代表元
        if fa[x] != x:
            fa[x] = self.find(fa[x])  # fa 改成代表元
        return fa[x]

    # 判断 x 和 y 是否在同一个集合
    def is_same(self, x: int, y: int) -> bool:
        # 如果 x 的代表元和 y 的代表元相同，那么 x 和 y 就在同一个集合
        # 这就是代表元的作用：用来快速判断两个元素是否在同一个集合
        return self.find(x) == self.find(y)

    # 把 from 所在集合合并到 to 所在集合中
    # 返回是否合并成功
    def merge(self, from_: int, to: int) -> bool:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return False
        self._fa[x] = y  # 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        self._size[y] += self._size[x]  # 更新集合大小（注意集合大小保存在代表元上）
        # 无需更新 _size[x]，因为我们不用 _size[x] 而是用 _size[find(x)] 获取集合大小，但 find(x) == y，我们不会再访问 _size[x]
        self.cc -= 1  # 成功合并，连通块个数减一
        return True

    # 返回 x 所在集合的大小
    def get_size(self, x: int) -> int:
        return self._size[self.find(x)]  # 集合大小保存在代表元上

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        uf = UnionFind(m * n)
        for i in range(m):
            d = dict()
            for j in range(n):
                x = matrix[i][j]
                idx = n * i + j
                if x in d:
                    uf.merge(idx, d[x])    
                else:
                    d[x] = idx
        for j in range(n):
            d = dict()
            for i in range(m):
                x = matrix[i][j]
                idx = n * i + j
                if x in d:
                    uf.merge(idx, d[x])
                else:
                    d[x] = idx
        
        g = dict()
        in_deg = defaultdict(int)

        for i in range(m):
            sorted_row = sorted((x, j) for j, x in enumerate(matrix[i]))
            for k, (v, j) in enumerate(sorted_row):
                fa = uf.find(i*n+j)
                if fa not in g:
                    g[fa] = set()
                if fa not in in_deg:
                    in_deg[fa] = 0
                if k + 1 < n and v < sorted_row[k + 1][0]:
                    curr_idx = i * n + j
                    nxt_idx = i * n + sorted_row[k + 1][1]
                    nxt_fa = uf.find(nxt_idx)
                    if nxt_fa not in g[fa]:
                        g[fa].add(nxt_fa)
                        in_deg[nxt_fa] += 1

        for j in range(n):
            sorted_col = sorted((matrix[i][j], i) for i in range(m))
            for k, (v, i) in enumerate(sorted_col):
                fa = uf.find(i*n+j)
                if fa not in g:
                    g[fa] = set()
                if fa not in in_deg:
                    in_deg[fa] = 0
                if k + 1 < m and v < sorted_col[k + 1][0]:
                    curr_idx = i * n + j
                    nxt_idx = sorted_col[k + 1][1] * n + j
                    nxt_fa = uf.find(nxt_idx)
                    if nxt_fa not in g[fa]:
                        g[fa].add(nxt_fa)
                        in_deg[nxt_fa] += 1
        
        rank = dict()
        q = deque()
        for fa, deg in in_deg.items():
            if deg == 0:
                q.append(fa)
                rank[fa] = 1
        
        
        while q:
            x = q.popleft()
            for y in g[x]:
                in_deg[y] -= 1
                if in_deg[y] == 0:
                    q.append(y)
                    rank[y] = max(rank.get(y, 1), rank[x] + 1)
        
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                fa = uf.find(i * n + j)
                ans[i][j] = rank[fa]
                
        return ans
        