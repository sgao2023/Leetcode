# https://leetcode.com/problems/build-a-matrix-with-conditions/description/
class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        row_g = [[] for _ in range(k)]
        col_g = [[] for _ in range(k)]
        r_in_deg = [0] * k
        c_in_deg = [0] * k
        for x, y in rowConditions:
            row_g[x - 1].append(y - 1)
            r_in_deg[y - 1] += 1
        for x, y in colConditions:
            col_g[x - 1].append(y - 1)
            c_in_deg[y - 1] += 1

        row_order = []
        col_order = []

        q = deque(i for i, deg in enumerate(r_in_deg) if deg == 0)
        while q:
            x = q.popleft()
            row_order.append(x)
            for y in row_g[x]:
                r_in_deg[y] -= 1
                if r_in_deg[y] == 0:
                    q.append(y)
        if len(row_order) != k:
            return []

        q = deque(i for i, deg in enumerate(c_in_deg) if deg == 0)
        while q:
            x = q.popleft()
            col_order.append(x)
            for y in col_g[x]:
                c_in_deg[y] -= 1
                if c_in_deg[y] == 0:
                    q.append(y)
        if len(col_order) != k:
            return []

        ans = [[0] * k for _ in range(k)]
        val_to_col = {v: i for i, v in enumerate(col_order)}
        for i, x in enumerate(row_order):
            ans[i][val_to_col[x]] = x + 1

        return ans