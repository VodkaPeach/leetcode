class UnionFind:
    def __init__(self, unique):
        self.root = {i:i for i in unique}
        self.rank = {i:1 for i in unique}
        # root / vertex
        self.div = {i:1 for i in unique}

    # return the root of x and div[x]
    def find(self, x):
        # if x not a root
        if self.root[x] != x:
            self.root[x], val = self.find(self.root[x])
            self.div[x] *= val
        return self.root[x], self.div[x]
    
    def union(self, x, y, d):
        rootX, divX = self.find(x)
        rootY, divY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]: self.union(y, x, 1/d)
            else:
                self.root[rootX] = self.root[rootY]
                self.div[rootX] = d * divY / divX
                self.rank[rootY] += 1

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        unique = set(sum(equations, []))
        uf = UnionFind(unique)
        
        for (u, v), w in zip(equations, values): uf.union(u, v, w)
        
        result = []
        for a, b in queries:
            if a in unique and b in unique:
                rootA, divA = uf.find(a)
                rootB, divB = uf.find(b)
                if rootA == rootB:
                    result.append(divA/divB)
                else: result.append(-1)
            else:
                result.append(-1)
        return result