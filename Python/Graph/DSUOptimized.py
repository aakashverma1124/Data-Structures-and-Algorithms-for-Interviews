class DSU:
    dsu_array = []
    def __init__(self, n):
        DSU.dsu_array = [[-1, 0]] * n
        self.n = n
    def find(self, v):
        print(DSU.dsu_array)
        if DSU.dsu_array[v][0] != -1:
            DSU.dsu_array[v][0] = self.find(DSU.dsu_array[v][0])
        return v
    def union(self, p1, p2):
        if DSU.dsu_array[p1][1] > DSU.dsu_array[p2][1]:
            DSU.dsu_array[p2][0] = p1
        elif DSU.dsu_array[p2][1] < DSU.dsu_array[p1][1]:
             DSU.dsu_array[p1][0] = p2
        else:
            DSU.dsu_array[p2][0] = p1
            DSU.dsu_array[p1][1] += 1
    def is_cycle(self, edges, n):
        for edge in edges:
            p1 = self.find(edge[0])
            p2 = self.find(edge[1])
            if p1 == p2:
                return True
            self.union(p1, p2)
        return False
if __name__ == "__main__":
    edges = [[0, 1], [0, 2]]
    dsu = DSU(3)
    print(dsu.is_cycle(edges, 3))