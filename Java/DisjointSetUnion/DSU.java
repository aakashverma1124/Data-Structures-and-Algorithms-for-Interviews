package Java.DisjointSetUnion;

class UnionFind {

    private int[] parent;

    public UnionFind(int size) {
        this.parent = new int[size];
        for(int i = 0; i < size; i++) {
            this.parent[i] = i;
        }
    }

    public int find(int u) {
        if(u == this.parent[u]) return u;
        return find(parent[u]);
    }

    public void union(int u, int v) {
        int p1 = find(u);
        int p2 = find(v);
        if(p1 != p2) {
            parent[p2] = p1;
        }
    }

    public boolean connected(int u, int v) {
        return find(u) == find(v);
    }

}

public class DSU {
    // int[][] edges = new int[][]{{0, 1}, {0, 2}, {1, 2}, {1, 3}, {2, 3}, {3, 4}};
    public static void main(String[] args) {
        UnionFind obj = new UnionFind(7);
        obj.union(0, 1);
        obj.union(0, 2);
        obj.union(1, 2);
        obj.union(1, 3);
        obj.union(2, 3);
        obj.union(3, 4);
        obj.union(5, 6); 
        System.out.println(obj.connected(1, 3));   
    }

}
