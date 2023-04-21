class DSU:

    dsu_array = []

    def __init__(self, n):
        DSU.dsu_array = [-1] * n
        self.n = n

    def find(self, v):
        if self.dsu_array[v] != -1:
            return self.find(DSU.dsu_array[v])
        return v

    def union(self, v1, v2):
        DSU.dsu_array[v2] = v1

    def is_cycle(self, edges, n):
        for edge in edges:
            p1 = self.find(edge[0])
            p2 = self.find(edge[1])
            if p1 == p2:
                return True
            self.union(edge[0], edge[1])
        return False

if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 3], [2, 4], [4, 5], [3, 5]]
    dsu = DSU(6)
    print(dsu.is_cycle(edges, 6))