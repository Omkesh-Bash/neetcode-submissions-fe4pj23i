
class Twitter:
    '''Solution 1'''
    def __init__(self):
        self.tweets = [] # (self.time, userId, tweetId)
        self.network = collections.defaultdict(set)
        self.time = 0
        # network = {}
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        # heapq.heappush(self.tweets, (self.time, userId, tweetId))
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        for user, tweetId in self.tweets[::-1]:
            if(len(result) >= 10):
                break
            if user == userId or user in self.network[userId]:
                result.append(tweetId)
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.network[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.network[followerId].discard(followeeId)
