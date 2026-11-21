from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}
        order = []
        stack = [(0, False)]

        while stack:
            u, exiting = stack.pop()
            c = s[u]
            if exiting:
                last[c].pop()
                continue
            order.append(u)
            if last.get(c):
                new_parent[u] = last[c][-1]

            last.setdefault(c, []).append(u)
            stack.append((u, True))
            for v in children[u]:
                stack.append((v, False))

        ans = [1] * n

        for u in reversed(order):
            p = new_parent[u]
            if p != -1:
                ans[p] += ans[u]
        return ans