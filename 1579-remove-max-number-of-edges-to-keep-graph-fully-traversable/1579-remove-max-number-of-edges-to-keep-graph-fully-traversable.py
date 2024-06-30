class UnionFind:
    def __init__(self, size):
        self.root = list(range(size+1))
        self.rank = [0] * (size+1)

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        
        if rootX == rootY: # if they have same root
            # node x, and y are already connected
            return False
        
        elif self.rank[rootX] < self.rank[rootY]: # if x has smaller root
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += self.rank[rootY]
        return True 

    
    
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        # initialize unionFind class
        uf = UnionFind(n)
        
        
        res = alice = bob = 0
        
        # first we deal with type 3, that allows both
        # alice and bob to traverse
        for typ, u, v in edges:
            if typ == 3:
                if uf.union(u, v): # if both  u and v nodes have same root
                    # we increment both, bcz type:3 can be traverse by both
                    # alice and bob
                    alice += 1
                    bob += 1
                else: # if rootsof u, v nodes are not connected
                    res += 1
        
        # apan copy bna lenge 3rd type edges ko connect krne k baad 
        # qki ab yha se hme dono k liye individually check krna hai ki saari
        # bachi nodes both alice & bob, dono ko reachable ko.. yani use node
        # par green and red dono lines ho.
        rootCopy = uf.root[:]
        
        
        # for alice, i.e type : 1
        for typ, u, v in edges:
            if typ == 1:
                if uf.union(u, v):
                    alice += 1 # since ye node sirf alice 
                else:
                    res += 1
        
        # alice k traversal k baad ham root ki value phir se usse stage pr
        # re-set krenge jab sirf type : 3 connections hue thay
        uf.root = rootCopy
        
        for typ, u, v in edges:
            if typ == 2:
                if uf.union(u, v): # agar dono node already connected h
                    bob += 1
                else:
                    res += 1
                    
        return res if alice == bob == n-1 else -1