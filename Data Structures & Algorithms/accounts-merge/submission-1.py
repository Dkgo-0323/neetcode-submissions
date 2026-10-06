from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first_email = account[1]

            graph[first_email]

            for email in account[2:]:
                graph[first_email].append(email)
                graph[email].append(first_email)
        
            for email in account[1:]:
                email_to_name[email] = name

        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, component)

        visited = set()
        res = []
        
        for email in graph:
            if email not in visited:
                component = []
                dfs(email, component)
                component.sort()
                name = email_to_name[email]
                res.append([name] + component)
        return res
