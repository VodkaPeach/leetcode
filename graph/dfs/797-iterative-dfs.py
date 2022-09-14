class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        stack = [(0, [0])]
        while stack:
            node, path = stack.pop()
            if node == len(graph)-1:
                paths.append(path)
            for i in graph[node]:
                stack.append((i, path+[i]))
        if not graph or len(graph) == 0:
            return paths
        return paths