class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def DFS(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    DFS(nei)
        count = 0
        for i in range(n):
            if i not in visited:
                DFS(i)
                count += 1
        return count