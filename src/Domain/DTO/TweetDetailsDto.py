from datetime import datetime


class TweetDetailsDto:

    def __init__(self, tweet_id: int, created_at: datetime, text: str,
                 followers_on_the_day: int, retweets: int, favorites: int):
        self.tweet_id = tweet_id
        self.created_at = created_at.isoformat()
        self.text = text
        self.followers_on_the_day = followers_on_the_day
        self.retweets = retweets
        self.favorites = favorites
