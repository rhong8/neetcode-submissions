class Twitter:

    def __init__(self):
        self.count = 0 #this is the global time
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        
        self.followMap[userId].add(userId)

        #print(f"Everyone that I'm following: {self.followMap[userId]}")

        
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                #the fourth value of the tuple: the next position we go to
                minHeap.append([count,tweetId,followeeId, index - 1])
        
        heapq.heapify(minHeap)
        
        while minHeap and len(res) < 10:
            #print(f"MinHeap at this moment: {minHeap}")
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,[count,tweetId,followeeId,index-1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)

        #discard: quiet remove
