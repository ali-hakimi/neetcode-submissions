class DSU {
    int[] par;
    int[] rank;

    public DSU(int n) {
        par = new int[n];
        rank = new int[n];
        Arrays.fill(rank, 1);
        for (int i = 0; i < par.length; i++) {
            par[i] = i;
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

    public boolean union(int n1, int n2) {
        int p1 = find(n1);
        int p2 = find(n2);

        if (p1 == p2) {
            return false;
        }

        if (this.rank[p2] > this.rank[p2]) {
            int temp = p1;
            p1 = p2;
            p2 = temp;
        }
        this.par[p2] = p1;
        rank[p1] += rank[p2];
        return true;
    }
}

class Solution {
    public int countComponents(int n, int[][] edges) {
        DSU dsu = new DSU(n);

        for (int[] edge: edges) {
            if (dsu.union(edge[0], edge[1])) {
                n--;
            }
        }
        return n;
    }
}
