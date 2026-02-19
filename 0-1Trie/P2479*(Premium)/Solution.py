class Node:
    __slots__ = 'children', 'cnt'

    def __init__(self):
        self.children = [None, None]
        self.cnt = 0  # 子树大小

class Trie:
    HIGH_BIT = 46

    def __init__(self):
        self.root = Node()

    # 添加 val
    def insert(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            if cur.children[bit] is None:
                cur.children[bit] = Node()
            cur = cur.children[bit]
            cur.cnt += 1  # 维护子树大小
        return cur

    # 删除 val，但不删除节点
    # 要求 val 必须在 trie 中
    def remove(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            cur = cur.children[(val >> i) & 1]
            cur.cnt -= 1  # 维护子树大小
        return cur

    # 返回 val 与 trie 中一个元素的最大异或和
    # 要求 trie 中至少有一个元素
    def max_xor(self, val: int) -> int:
        cur = self.root
        ans = 0
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            # 如果 cur.children[bit^1].cnt == 0，视作空节点
            if cur.children[bit ^ 1] and cur.children[bit ^ 1].cnt:
                ans |= 1 << i
                bit ^= 1
            cur = cur.children[bit]
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-strong-pair-xor-ii/solutions/2523213/0-1-trie-hua-dong-chuang-kou-pythonjavac-gvv2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        subtree_sum = [0] * n
        
        def get_sum(node, fa):
            res = values[node]
            for son in g[node]:
                if son == fa:
                    continue
                res += get_sum(son, node)
            subtree_sum[node] = res
            return res
        
        get_sum(0, -1)

        t = Trie()
        ans = 0
        trie_empty = True
        def dfs(node, fa):
            nonlocal ans
            nonlocal trie_empty
            if not trie_empty:
                ans = max(ans, t.max_xor(subtree_sum[node]))
            for son in g[node]:
                if son == fa:
                    continue
                dfs(son, node)

            t.insert(subtree_sum[node])
            trie_empty = False
        
        dfs(0, -1)

        return ans