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
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
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
        cc = []
        sss = list(s)
        for a, b in pairs:
            uf.union(a,b)
        for i in range(len(s)):
            uf.root[i] = uf.find(i)
        # unique roots for connected components
        for r in uf.root:
            if r not in cc:
                cc.append(r)
        
        # component[] contains each component as a list of indices
        # [[0,3],[1,2]]
        component=[]
        for c in cc:
            # indices of each component
            component.append([i for i in uf.root if uf.root[i]==c])
        
        for j in component:
            # truecomp=[3,0]
            # j=[0,3]
            truecomp = j
            truecomp.sort(key=lambda x: s[x], reverse=True)
            for i in range(len(j)):
                sss[j[i]]=s[truecomp[i]]
        return str(sss)