class DSU {
    int[] par;
    int[] rank;

    public DSU(int n) {
        this.par = new int[n];
        this.rank = new int[n];

        for (int i = 0; i < n; i++) {
            this.par[i] = i;
            this.rank[i] = 1;
        }
    }

    public int find(int node) {
        int cur = node;
        while (cur != this.par[cur]) {
            this.par[cur] = this.par[this.par[cur]];
            cur = this.par[cur];
        }
        return cur;
    }

    public boolean union(int u, int v) {
        int pu = find(u);
        int pv = find(v);
        
        if (pu == pv) {
            return false;
        }

        if (rank[pv] > rank[pu]) {
            int temp = pu;
            pu = pv;
            pv = temp;
        }

        par[pv] = pu;
        rank[pu] += rank[pv];
        return true;
    }
}

class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        DSU dsu = new DSU(edges.length + 1);

        for (int[] edge: edges) {
            if (!dsu.union(edge[0], edge[1])) {
                return edge;
            }
        }
        return new int[0];
    }
}
