class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = [False] * n
        def dfs(node):
            for nei in adjList[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visited[node]:
                visited[node] = True
                dfs(node)
                res += 1

        return res