class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        uf = UnionFind(n)
        for x, y in edges:
            if not uf.union(x,y):
                return False
        return True

class UnionFind:
    def __init__(self, size):
        self.rank = [1]*size
        self.root = [i for i in range(size)]
    
    def find(self, x):
        if self.root[x]==x:
            return x
        self.root[x] = self.find(root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootX = self.root[x]
        rootY = self.root[y]
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX]+=1
            return True
        return False