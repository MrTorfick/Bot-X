import os
import tweepy
from datetime import date
import logging
import sys


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger()

def post_daily_tweet():
    try:

        release_date = date(2026, 5, 26)
        today = date.today()
        days_left = (release_date - today).days


        tweet = f"There are {days_left} days left until the release of GTA 6."
        

        client = tweepy.Client(
            consumer_key=os.getenv("API_KEY"),
            consumer_secret=os.getenv("API_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            access_token_secret=os.getenv("ACCESS_SECRET")
        )
        
        response = client.create_tweet(text=tweet)
        logger.info(f"Tweet publicado exitosamente: {tweet}")
        
    except Exception as e:
        logger.error(f"Error al publicar el tweet: {e}")
        sys.exit(1)

if __name__ == "__main__":
    post_daily_tweet()