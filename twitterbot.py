import tweepy
import time

CONSUMER_KEY = 'XXX'
CONSUMER_SECRET = 'XXX'
ACCESS_KEY = 'XXX'
ACCESS_SECRET = 'XXX'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

twitter_API = tweepy.API(auth)

for status in tweepy.Cursor(twitter_API.user_timeline).items():
    try:
        twitter_API.destroy_status(status.id)
    except:
        pass

##Lista de seguidores
followers = twitter_API.followers()
def mention_followers():
    for follower in followers:
        print(follower.screen_name)
        twitter_API.update_status('Hello 2 @' + follower.screen_name)

##Llamamos a la funcion en un bucle infinito:
while True:
   mention_followers()
   time.sleep(3600)
