class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != len(edges)+1:
            return False

        adjList = defaultdict(list)
        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        q = deque([0])
        visited = set()

        while q:
            node = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            for nei in adjList[node]:
                if nei not in visited:
                    q.append(nei)

        return len(visited) == n