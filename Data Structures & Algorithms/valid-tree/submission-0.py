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
            if node not in visited:
                visited.add(node)
                for nei in graph[node]:
                    DFS(nei)
        DFS(0)

        return len(visited) == n