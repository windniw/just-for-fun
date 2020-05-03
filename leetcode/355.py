"""

link: https://leetcode.com/problems/design-twitter

problem: 设计推特，支持订阅，发送，关注功能

solution: 用集合字典模拟数据库。

"""
class Twitter:
    class TwitterData:
        def __init__(self, id, timestamp):
            self.id = id
            self.timestamp = timestamp

    class User:
        def __init__(self):
            self.follows = set()
            self.twitters = []

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamp = 0
        self.users = collections.defaultdict(self.User)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.users[userId].twitters.append(self.TwitterData(tweetId, self.timestamp))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        user = self.users[userId]
        res = []
        res.extend(user.twitters)
        for x in user.follows:
            res.extend(self.users[x].twitters)
        res.sort(key=lambda x: -x.timestamp)
        return [x.id for x in res][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId or followeeId in self.users[followerId].follows:
            return
        self.users[followerId].follows.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.users[followerId].follows:
            return
        self.users[followerId].follows.remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)