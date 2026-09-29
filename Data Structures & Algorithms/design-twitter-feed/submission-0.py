class Twitter:

    def __init__(self):

        self.count = 0 # time to track when tweet was posted
        self.tweetmap = defaultdict(list) # user id to list [count, tweetid]
        self.followmap = defaultdict(set) # user id to people who he follows
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweetmap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        minHeap = []
        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:

            if followeeId in self.tweetmap:
                index = len(self.tweetmap[followeeId]) - 1
                count, tweetId = self.tweetmap[followeeId][index]

                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetmap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.followmap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        
