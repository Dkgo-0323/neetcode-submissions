class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = [[] for _ in range(n)] # 邻接表

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def DFS(node: int) -> None:
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    DFS(nei)
        DFS(0)

        return len(visited) == n