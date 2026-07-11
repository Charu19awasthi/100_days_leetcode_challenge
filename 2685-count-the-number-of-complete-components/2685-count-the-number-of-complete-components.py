class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # Create adjacency list
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        ans = 0
        
        def dfs(node):
            visited[node] = True
            vertices = 1
            edge_count = len(graph[node])
            
            for nei in graph[node]:
                if not visited[nei]:
                    v, e = dfs(nei)
                    vertices += v
                    edge_count += e
            
            return vertices, edge_count
        
        for i in range(n):
            if not visited[i]:
                vertices, edges_count = dfs(i)
                
                # Every edge is counted twice
                edges_count //= 2
                
                # Complete graph condition
                if edges_count == vertices * (vertices - 1) // 2:
                    ans += 1
        
        return ans