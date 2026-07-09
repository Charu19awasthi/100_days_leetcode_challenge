class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # Build connections
        for i in range(n - 1):
            if nums[i+1] - nums[i] <= maxDiff:
                union(i, i+1)

        # Answer queries
        result = []
        for u, v in queries:
            result.append(find(u) == find(v))

        return result