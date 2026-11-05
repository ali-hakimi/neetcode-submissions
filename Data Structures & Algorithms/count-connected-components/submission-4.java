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
            cur = this.par[this.par[cur]];
        }
        return cur;
    }

    public boolean union(int n1, int n2) {
        int p1 = find(n1);
        int p2 = find(n2);
        if (p1 == p2) {
            return false;
        }

        if (this.rank[p2] > this.rank[p1]) {
            int temp = p1;
            p1 = p2;
            p2 = temp;
        }

        this.par[p2] = p1;
        this.rank[p1] += this.rank[p2];
        return true;
    }
}

class Solution {
    public int countComponents(int n, int[][] edges) {
        DSU dsu = new DSU(n + 1);
        for (int[] edge: edges) {
            int n1 = edge[0];
            int n2 = edge[1];

            if (dsu.union(n1, n2)) {
                n--;
            }
        }
        return n;
    }
}
