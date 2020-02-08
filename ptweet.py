#
#
#

import random
import tweepy
import time
import configparser

config = configparser.ConfigParser()
config.read('configure.ini')

CONSUMER_KEY = config.get('TWITTER', 'CONSUMER_KEY')
CONSUMER_SECRET = config.get('TWITTER', 'CONSUMER_SECRET')
ACCESS_TOKEN = config.get('TWITTER', 'ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config.get('TWITTER', 'ACCESS_TOKEN_SECRET')

WORDS = config.get('TWITTER', 'WORDS')

tweet_data = open("sentences.txt", 'r')
list_text = tweet_data.readlines()
list_text_sampled = random.sample(list_text, len(list_text))

def post_tweet(text):

  try:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(status = text)
  except tweepy.TweepError as e:
    print(e.reason)


if __name__ == '__main__':
#  post_tweet('自動生成つぶやきのテストします。')

  for tweet in list_text_sampled:
    tweet_message = tweet.rstrip("\n") + WORDS
    print(tweet_message)
    post_tweet(tweet_message)
    time.sleep(3600)
