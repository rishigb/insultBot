import tweepy
import time

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def tweetIt(_text):
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "nZNaBHqEUFIVNeFBUUjFQWa3c",
    "consumer_secret"     : "ltjmhAUnl6xbQa8ZzSW7XkM0heciSoO5YDMoGVjfpaw6nPoENe",
    "access_token"        : "124088888-9bFnLQjsZTeGyKiZqYHyQ05ZsJkG9eaD4CywRd08",
    "access_token_secret" : "FXmtMaItnfXvFx5ybO8L6SIwO95TV58dhLmnTxAy01LfN"
    }

  api = get_api(cfg)
  tweet = _text
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

#if __name__ == "__main__":
#  main()
#tweetIt("It looks like it is raining in #Bangalore.")

#listOfTweets={"tweet1":"Cant make an omlette without breaking a few eggs bro. #gyan","tweet2":"Maybe I shouldn't think about food when I am expanding like the universe."}

for i in range(0,5):
    textForTweeting ="Don't think about food attempt number " + str(i+1) +"."
    print ((textForTweeting))
    time.sleep(2)
    #tweetIt(str(textForTweeting))
