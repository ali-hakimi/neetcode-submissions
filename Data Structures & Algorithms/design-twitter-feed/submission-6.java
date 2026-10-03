class Twitter {
    private Map<Integer, Set<Integer>> followerMap;
    private int time;
    private Map<Integer, List<int[]>> tweetMap;
    public Twitter() {
        this.followerMap = new HashMap<>();
        this.time = 0;
        this.tweetMap = new HashMap<>();
    }

    public void postTweet(int userId, int tweetId) {
        if (!this.tweetMap.containsKey(userId)) {
            this.tweetMap.put(userId, new ArrayList<>());
        }
        this.tweetMap.get(userId).add(new int[] {time++, tweetId});
    }

    public List<Integer> getNewsFeed(int userId) {
        Set<Integer> followees = this.followerMap.getOrDefault(userId, new HashSet<>());
        followees.add(userId);

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        for (int followee : followees) {
            List<int[]> tweets = this.tweetMap.getOrDefault(followee, new ArrayList<>());
            for (int[] tweet : tweets) {
                pq.offer(tweet);
            }
        }

        List<Integer> res = new ArrayList<>();
        int n = 0;
        while (!pq.isEmpty() && n < 10) {
            res.add(pq.poll()[1]);
            n++;
        }
        return res;
    }

    public void follow(int followerId, int followeeId) {
        if (!this.followerMap.containsKey(followerId)) {
            this.followerMap.put(followerId, new HashSet<>());
        }
        this.followerMap.get(followerId).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        if (!this.followerMap.containsKey(followerId)) {
            return;
        }
        this.followerMap.get(followerId).remove(followeeId);
    }
}
