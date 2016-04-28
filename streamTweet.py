import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import xlrd
import xlwt

consumer_key = "nZNaBHqEUFIVNeFBUUjFQWa3c"
consumer_secret= "ltjmhAUnl6xbQa8ZzSW7XkM0heciSoO5YDMoGVjfpaw6nPoENe"
access_token = "124088888-9bFnLQjsZTeGyKiZqYHyQ05ZsJkG9eaD4CywRd08"
access_token_secret = "FXmtMaItnfXvFx5ybO8L6SIwO95TV58dhLmnTxAy01LfN"


fo = open("dataRevAll.csv", "wb")
fo.write(str("Name"+"|"+"Tweet"+"|"+"PersonDescription"+"|"+"Following"+"|"+"Followers"+"|"+"statusCount"+"|"+"retweet_count"+"|"+"verified"+"|"+"LocationOfOriginOfTweet"+"|"+"lang")+ str(os.linesep))
'''
status.user.screen_name
status.text
status.user.description
status.user.location -- not accurate
status.user.verified (true or false)
status.user.followers_count
--status.user.created_at
status.user.statuses_count
status.retweet_count
status.user.friends_count
---
status.place -- gives data sometimes, doesn't other times.
status.place.country -- not working
status.place.full_name-- not
status.place.name -- not
status.place.place_type --not
status.place.url -- not
--Doesn't work -- status.coordinates.coordinates (longitude and latitude)
'''

class listener(StreamListener):
    
    ''' On status worked better than on_data. The json format can be directly used here '''
   
        def on_status(self, status):
            try:
                tweet = status.user.screen_name+ status.text
                print (tweet)
                fo.write(status.user.screen_name)
                opSheet.write(j,1,status.text)
                opSheet.write(j,2,status.user.description)
                opSheet.write(j,3,status.user.friends_count)
                opSheet.write(j,4,status.user.followers_count)
                opSheet.write(j,5,status.user.statuses_count)
                opSheet.write(j,6,status.retweet_count)
                opSheet.write(j,7,status.user.verified)
                opSheet.write(j,8,status.user.location)
                opSheet.write(j,9,status.lang)
                
                




            except : #Called on any exception
                fw.save("TargetApparelFriday"+".xls")
                print ('failed on data'),str(e)
                #time.sleep(2)
    on_event = on_status

    def on_error(self, status):
        print (status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
''' Wait for the input '''
#__track = raw_input("Enter something you want to track: ")
twitterStream = Stream(auth, listener())
''' Enter the string that needs to be tracked '''
twitterStream.filter(track=["pussy"], async=True)
