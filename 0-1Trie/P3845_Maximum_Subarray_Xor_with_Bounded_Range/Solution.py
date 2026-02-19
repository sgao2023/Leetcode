from sortedcontainers import SortedList
class Node:
    __slots__ = 'children', 'cnt'

    def __init__(self):
        self.children = [None, None]
        self.cnt = 0  # 子树大小

class Trie:
    HIGH_BIT = 15

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
    def maxXor(self, nums: list[int], k: int) -> int:
        prefix_xor = [0]
        for x in nums:
            prefix_xor.append(prefix_xor[-1] ^ x)
        trie_prefix_xor = Trie()
        sl = SortedList()
        trie_prefix_xor.insert(0)
        l = 0
        ans = 0
        for r, x in enumerate(nums):
            sl.add(x)
            trie_prefix_xor.insert(prefix_xor[r + 1])
            while sl[-1] - sl[0] > k:
                sl.remove(nums[l])
                trie_prefix_xor.remove(prefix_xor[l])
                l += 1
            
            ans = max(ans, trie_prefix_xor.max_xor(prefix_xor[r+1]))
        
        return ans