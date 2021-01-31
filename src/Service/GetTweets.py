import tweepy
from tweepy import TweepError, RateLimitError

from src.Domain.DTO.ParametersDto import ParametersDto
from src.Domain.DTO.TweetDetailsDto import TweetDetailsDto
from src.Domain.DTO.TweetDto import TweetDto
from src.Domain.Exception.TweetNotFoundException import TweetNotFoundException
from src.Domain.Exception.TwitterConnectionException import TwitterConnectionException
from src.Infrastructure.CrossCutting.TwitterApi.TwitterConnection import TwitterConnection


class GetTweets:

    def get_tweets_by_user_name(self, parameters: ParametersDto) -> TweetDto:
        try:
            twitter_connection = TwitterConnection.connect()
            tweets_search = tweepy.Cursor(twitter_connection.search,
                                          q=f"from:{parameters.get_name()} -filter:retweets",
                                          since=parameters.get_date_since()).items(parameters.get_limit())
            tweets_details = []
            user_created = user_id = user_name = None

            for tweet_search in tweets_search:
                user_id = tweet_search.user.id
                user_created = tweet_search.user.created_at
                user_name = tweet_search.user.name

                tweets_details.append(TweetDetailsDto(
                    tweet_search.id,
                    tweet_search.created_at,
                    tweet_search.text,
                    tweet_search.user.followers_count,
                    tweet_search.retweet_count,
                    tweet_search.favorite_count,
                ))

            if not tweets_details:
                raise TweetNotFoundException()

            return TweetDto(user_id, user_name, user_created, tweets_details)

        except (TweepError, RateLimitError):
            raise TwitterConnectionException()
