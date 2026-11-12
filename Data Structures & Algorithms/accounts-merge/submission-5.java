class DSU {
    int[] par;
    int[] rank;

    public DSU(int n) {
        par = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            par[i] = i;
            rank[i] = 1;
        }
    }

    public int find(int n1) {
        int cur = n1;
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
        if (rank[p2] > rank[p1]) {
            int temp = p1;
            p1 = p2;
            p2 = temp;
        }
        par[p2] = p1;
        rank[p1] += rank[p2];
        return true;
    }
}

class Solution {
    Map<String, Integer> emailToAccount = new HashMap<>();
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        DSU dsu = new DSU(accounts.size());
        for (int i = 0; i < accounts.size(); i++) {
            List<String> account = accounts.get(i);
            for (int j = 1; j < account.size(); j++) {
                String email = account.get(j);
                if (emailToAccount.containsKey(email)) {
                    int n1 = emailToAccount.get(email);
                    int n2 = i;
                    dsu.union(n1, n2);
                } else {
                    emailToAccount.put(email, i);
                }
            }
        }

        Map<Integer, List<String>> mergeEmails = new HashMap<>();
        List<List<String>> res = new ArrayList<>();

        for (String email : emailToAccount.keySet()) {
            int parent = dsu.find(emailToAccount.get(email));
            mergeEmails.computeIfAbsent(parent, k -> new ArrayList<>()).add(email);
        }

        for (int acctNumber : mergeEmails.keySet()) {
            List<String> account = new ArrayList<>();
            account.add(accounts.get(acctNumber).get(0));
            account.addAll(mergeEmails.get(acctNumber));
            res.add(account);
        }
        return res;
    }
}