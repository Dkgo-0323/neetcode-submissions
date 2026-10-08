from collections import deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return ""
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        queue = deque()
        order = ""
        for c, i in indegree.items():
            if i == 0:
                queue.append(c)
        
        while queue:
            ch = queue.popleft()
            order += ch
            for nei in graph[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return order if len(order) == len(graph) else ""