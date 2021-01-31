from datetime import datetime
from typing import List

from src.Domain.DTO.TweetDetailsDto import TweetDetailsDto


class TweetDto:

    def __init__(self, user_id: int, user_name: str, user_created_at: datetime, user_tweets: List[TweetDetailsDto]):
        self.user_id = user_id
        self.user_name = user_name
        self.user_created_at = user_created_at.isoformat()
        self.user_tweets = user_tweets

    def to_table(self) -> list:
        tweet_table = []

        for tweet_details in self.user_tweets:
            tweet_table.append({
                "user_id": self.user_id,
                "user_name": self.user_name,
                "user_created_at": self.user_created_at,
                "id": tweet_details.tweet_id,
                "created_at": tweet_details.created_at,
                "text": tweet_details.text,
                "followers_on_the_day": tweet_details.followers_on_the_day,
                "retweets": tweet_details.retweets,
                "favorites": tweet_details.favorites
            })
        return tweet_table
