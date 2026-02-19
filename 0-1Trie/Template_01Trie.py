# 0-1 Trie 模板
# 可以解决数组中两数最大异或和，或者异或和在某个范围内的数对个数等问题
# 区间最大异或和可以转化成前缀和，本质也是两数最大异或和问题
# 求最大异或和使用max_xor
# 求最大异或和至少为 target 使用count_at_least
# 求最大异或和在low和high之间，等价于 count_at_least(val, low) - count_at_least(val, high + 1)

class Node:
    __slots__ = 'children', 'cnt'

    def __init__(self):
        self.children = [None, None]
        self.cnt = 0  # 子树大小

class Trie:
    # 此处根据实际情况调整
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

    # 这个函数是我自己写的
    # 可能变量名和函数名需要改进，但目前为止没出过问题
    # 返回 trie 中元素与 val 的异或和至少为 (>=) target 的元素个数
    def count_at_least(self, val, target):
        cur = self.root
        ans = 0
        for i in range(Trie.HIGH_BIT, -1, -1):
            # val 的第 i 位
            bit = (val >> i) & 1
            # target 的第 i 位
            tar_bit = (target >> i) & 1
            # 下一个节点，沿着这条路走，那么和val做xor可以得到target 
            nxt_bit = bit ^ tar_bit

            # 找（得到的异或结果）比 target 当前位更大（不小于）的情况
            # 如果 target 当前位为 1，只能往 nxt_bit 走
            if tar_bit == 1:
                if not (cur.children[nxt_bit] and cur.children[nxt_bit].cnt):
                    break
            # 如果 target 当前位为 0，可以往 nxt_bit 走，也可以往 nxt_bit^1 走
            # （也就是说这一位上的结果可以是1 也可以是0， 对应的就是nxt_bit和nxt_bit^1）
            # 如果往 nxt_bit^1 走，那么和 val 做 xor 可以得到比 target 大的数，
            # 那个分支里的所有数都满足条件，把那个分支的cnt加入答案
            else:
                if cur.children[nxt_bit ^ 1] is not None:
                    ans += cur.children[nxt_bit ^ 1].cnt
            # 沿着nxt_bit走
            cur = cur.children[nxt_bit]

            # 没有路了就停
            if cur is None:
                break
            # 如果走到第0位了，说明找到了和val做xor恰好等于target的数，这也要计入答案
            # 注意：由于Trie里的数字可以有重复，所以ans不止是加一，而是加上那个节点的cnt
            if i == 0:
                ans += cur.cnt
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximum-strong-pair-xor-ii/solutions/2523213/0-1-trie-hua-dong-chuang-kou-pythonjavac-gvv2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。