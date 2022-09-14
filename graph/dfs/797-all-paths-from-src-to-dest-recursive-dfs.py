class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        path = []
        def dfs(node):
            path.append(node)
            if node == len(graph)-1:
                paths.append(path.copy())
                return
            for i in graph[node]:
                dfs(i)
                path.pop()
        if not graph or len(graph) == 0:
            return paths
        dfs(0)
        return paths