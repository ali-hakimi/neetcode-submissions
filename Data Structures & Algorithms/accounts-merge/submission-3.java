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

    public int find(int n) {
        int cur = n;
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
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, Integer> emailToAccount = new HashMap<>();
        DSU dsu = new DSU(accounts.size());

        for (int i = 0; i < accounts.size(); i++) {
            List<String> account = accounts.get(i);
            for (int j = 1; j < account.size(); j++) {
                if (emailToAccount.containsKey(account.get(j))) {
                    int n1 = emailToAccount.get(account.get(j));
                    int n2 = i;
                    dsu.union(n1,n2);

                }
                else {
                    emailToAccount.put(account.get(j), i);
                }
            }
        }

        Map<Integer, Set<String>> mergedEmails = new HashMap<>();


        for (int i = 0; i < accounts.size(); i++) {
            int par = dsu.find(i);
            if (!mergedEmails.containsKey(par)) {
                mergedEmails.put(par, new HashSet<>());
            }
            List<String> accountEmails = accounts.get(i).subList(1, accounts.get(i).size());
            mergedEmails.get(par).addAll(accountEmails);
        }
        System.out.println(mergedEmails);

        List<List<String>> res = new ArrayList<>();
        for (Map.Entry<Integer, Set<String>> entry: mergedEmails.entrySet()) {
            List<String> acct = new ArrayList<>();
            acct.add(accounts.get(entry.getKey()).get(0));
            acct.addAll(entry.getValue());
            res.add(acct);
        }

        return res;
    }
}