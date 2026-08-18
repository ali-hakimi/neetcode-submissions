class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        followees = self.followMap[userId]
        followees.add(userId)
        for followee in followees:
            if followee in self.tweetMap:
                idx = len(self.tweetMap[followee]) - 1
                cnt, tweetId = self.tweetMap[followee][idx]
                minHeap.append((cnt, tweetId, followee, idx))
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            cnt, tweetId, followee, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx:
                cnt, tweetId = self.tweetMap[followee][idx-1]
                heapq.heappush(minHeap, (cnt, tweetId, followee, idx-1))
        return res       

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
