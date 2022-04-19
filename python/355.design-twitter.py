#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
from typing import List

# @lc code=start
class Twitter:
    
    def __init__(self):
        self.tweets = []
        self.users = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users.append(userId)
        
        self.tweets.insert(0, (userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.users.append(userId)
        
        target_users = [userId]
        feed = []

        if userId in self.follows:
            target_users.extend(self.follows[userId])

        for tweet in self.tweets:
            if tweet[0] in target_users:
                feed.append(tweet[1])

                if len(feed) == 10:
                    break
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users.append(followerId)
        if followeeId not in self.users:
            self.users.append(followeeId)

        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                pass
            else:
                self.follows[followerId].append(followeeId)
        else:
            self.follows[followerId] = [ followeeId ]
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users.append(followerId)
        if followeeId not in self.users:
            self.users.append(followeeId)

        if followerId in self.follows:
            if followeeId in self.follows[followerId]:
                self.follows[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

