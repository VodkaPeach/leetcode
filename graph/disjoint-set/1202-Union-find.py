class UnionFind:
    def __init__(self, s):
        self.root = [i for i in range(len(s))]
        self.rank = [1]*len(s)
        self.str = s
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX]+=1
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf=UnionFind(s)
        groups = defaultdict(list)
        # union
        for a, b in pairs:
            uf.union(a,b)
        
        # path compression
        for i in range(len(s)):
            uf.root[i] = uf.find(i)
        
        # unique roots for connected components
        for i in range(len(uf.root)):
            groups[uf.root[i]].append(s[i])
        for key in groups.keys():
            groups[key].sort(reverse=True)
            
        result = []
        for i in range(len(s)):
            result.append(groups[uf.root[i]].pop())
        r = ''.join(result)
        return r