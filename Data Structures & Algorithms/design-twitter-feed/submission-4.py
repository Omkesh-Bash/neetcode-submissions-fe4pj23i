class Twitter:
    '''Solution 4'''
    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.network = collections.defaultdict(set)
        self.time = 0
        # network = {}
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        # heapq.heappush(self.tweets, (self.time, userId, tweetId))
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        minHeap = [] # we will make it work as max heap  

        # add all followee's last tweet to minheap
        self.network[userId].add(userId) # for this problem. It is set so no worry for duplicate calls
        for followee in self.network[userId]:
            if followee in self.tweets: # -------------IF no tweet by that followee 
                index = len(self.tweets[followee]) - 1 # last index
                time, tweetId = self.tweets[followee][index]
                minHeap.append((time, tweetId, followee, index - 1)) # next most recent (second last).
        heapq.heapify(minHeap) # overall bit lesser time as compared to heapifyAdd for large number of followees

        # loop same till result
        while minHeap and len(result) < 10: #------------------- IF any of these fail 
            time, tweetId, followee, index = heapq.heappop(minHeap)
            result.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[followee][index]
                heapq.heappush(minHeap, (time, tweetId, followee, index - 1))
        
        return result

        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.network[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.network[followerId].discard(followeeId)

